"""
Test script to verify Anthropic and OpenAI direct API connections
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
import anthropic
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API keys from environment
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

def test_anthropic():
    """Test Anthropic Claude API connection"""
    print("="*80)
    print("TEST 1: Anthropic Claude API")
    print("="*80)
    print("Model: claude-3-sonnet-20240229")
    
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        print("\nSending test message...")
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Say 'Anthropic connection successful!'"}
            ]
        )
        
        # Get text from response
        result = ""
        for block in response.content:
            if hasattr(block, 'text'):
                result = str(getattr(block, 'text', ''))
                break
        
        print(f"✓ Anthropic API working!")
        print(f"  Response: {result}")
        print(f"  Model: {response.model}")
        print(f"  Tokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
        return True
        
    except anthropic.AuthenticationError:
        print("✗ Authentication failed!")
        print("  → Check ANTHROPIC_API_KEY in .env file")
        print("  → Verify key at https://console.anthropic.com/settings/keys")
        return False
    except anthropic.RateLimitError:
        print("✗ Rate limit exceeded!")
        print("  → Wait a moment and try again")
        print("  → Check usage at https://console.anthropic.com/settings/usage")
        return False
    except Exception as e:
        print(f"✗ Anthropic API failed: {type(e).__name__}")
        print(f"  Error: {str(e)}")
        return False

def test_openai():
    """Test OpenAI GPT API connection"""
    print("\n" + "="*80)
    print("TEST 2: OpenAI GPT API")
    print("="*80)
    print("Model: gpt-4o-mini")
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        print("\nSending test message...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Say 'OpenAI connection successful!'"}
            ]
        )
        
        result = response.choices[0].message.content
        print(f"✓ OpenAI API working!")
        print(f"  Response: {result}")
        print(f"  Model: {response.model}")
        if response.usage:
            print(f"  Tokens used: {response.usage.prompt_tokens} in, {response.usage.completion_tokens} out")
        return True
        
    except Exception as e:
        error_str = str(e)
        print(f"✗ OpenAI API failed: {type(e).__name__}")
        
        if "401" in error_str or "Incorrect API key" in error_str:
            print("  → Check OPENAI_API_KEY in .env file")
            print("  → Verify key at https://platform.openai.com/api-keys")
        elif "429" in error_str:
            print("  → Rate limit exceeded")
            print("  → Check usage at https://platform.openai.com/usage")
        elif "404" in error_str:
            print("  → Model not found or access denied")
            print("  → Verify 'gpt-4o-mini' is available to your account")
        else:
            print(f"  Error: {error_str}")
        
        return False

def test_embedding_service():
    """Test embedding generation for RAG"""
    print("\n" + "="*80)
    print("TEST 3: Embedding Service (for RAG)")
    print("="*80)
    
    try:
        # Your system uses sentence-transformers for embeddings
        from sentence_transformers import SentenceTransformer
        
        print("Loading embedding model...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        print("Generating test embedding...")
        embedding = model.encode("Test sentence for embedding")
        
        print(f"✓ Embedding service working!")
        print(f"  Model: all-MiniLM-L6-v2")
        print(f"  Embedding dimensions: {len(embedding)}")
        return True
        
    except Exception as e:
        print(f"✗ Embedding service failed: {type(e).__name__}")
        print(f"  Error: {str(e)}")
        print("  → Ensure sentence-transformers is installed:")
        print("     pip install sentence-transformers")
        return False

def test_internet_connectivity():
    """Test basic internet connectivity"""
    print("\n" + "="*80)
    print("TEST 4: Internet Connectivity")
    print("="*80)
    
    import socket
    
    endpoints = [
        ("api.anthropic.com", 443, "Anthropic API"),
        ("api.openai.com", 443, "OpenAI API"),
        ("huggingface.co", 443, "HuggingFace (for embeddings)"),
        ("8.8.8.8", 53, "Internet (Google DNS)")
    ]
    
    all_ok = True
    for host, port, name in endpoints:
        try:
            socket.create_connection((host, port), timeout=5)
            print(f"✓ Can reach {name} ({host}:{port})")
        except Exception as e:
            print(f"✗ Cannot reach {name} ({host}:{port})")
            print(f"  Error: {type(e).__name__}")
            all_ok = False
    
    return all_ok

def main():
    """Run all diagnostic tests"""
    print("="*80)
    print("RAG TEST CASE GENERATION SYSTEM - API DIAGNOSTICS")
    print("="*80)
    print("\nTesting connections to:")
    print("  • Anthropic Claude (primary LLM)")
    print("  • OpenAI GPT (fallback LLM)")
    print("  • Sentence Transformers (embeddings)")
    print("  • Internet connectivity")
    
    results = {
        "Internet": test_internet_connectivity(),
        "Anthropic": test_anthropic(),
        "OpenAI": test_openai(),
        "Embeddings": test_embedding_service()
    }
    
    print("\n" + "="*80)
    print("DIAGNOSTIC SUMMARY")
    print("="*80)
    
    for test, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {test:20} {status}")
    
    print("\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)
    
    if not results["Internet"]:
        print("\nCRITICAL: No internet connectivity")
        print("   1. Check your network connection")
        print("   2. Verify firewall/proxy settings")
        print("   3. Try: ping google.com")
        
    elif not results["Anthropic"] and not results["OpenAI"]:
        print("\n CRITICAL: Both LLM APIs failed")
        print("   1. Check API keys in .env file")
        print("   2. Verify keys haven't expired")
        print("   3. Check account billing/credits")
        
    elif not results["Anthropic"]:
        print("\n🟡 WARNING: Anthropic API failed (will use OpenAI fallback)")
        print("   1. Check ANTHROPIC_API_KEY in .env")
        print("   2. Verify at https://console.anthropic.com/")
        print("   3. System will use OpenAI as fallback")
        
    elif not results["OpenAI"]:
        print("\n🟡 WARNING: OpenAI API failed (Anthropic is working)")
        print("   1. Check OPENAI_API_KEY in .env")
        print("   2. Verify at https://platform.openai.com/api-keys")
        print("   3. System will use Anthropic exclusively")
        
    elif not results["Embeddings"]:
        print("\n🟡 WARNING: Embedding service failed")
        print("   1. Install: pip install sentence-transformers")
        print("   2. May need: pip install torch")
        print("   3. RAG search won't work without embeddings")
        
    else:
        print("\n✅ ALL SYSTEMS GO!")
        print("   • Both LLM APIs are working")
        print("   • Embedding service is operational")
        print("   • Internet connectivity is stable")
        print("\n   Your RAG test case generation system is ready!")
    
    print("\n" + "="*80)
    
    return all(results.values())

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
