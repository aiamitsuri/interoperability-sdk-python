#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjiramramju
#ramramjiramramjiramramju
#ramramjiramramjiramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjiramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji

import interoperability_wrapper_pyo3 as sdk
import json
import asyncio

async def fetch_interop(json_str: str) -> str:
    params = json.loads(json_str)
    res = sdk.fetch_from_python(json.dumps(params))
    return json.dumps(json.loads(res), indent=2)

async def main():
    try:
        print("Python SDK")
        result = await fetch_interop('{"page": "1"}')
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
    
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjiramramju
#ramramjiramramjiramramju
#ramramjiramramjiramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjiramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji