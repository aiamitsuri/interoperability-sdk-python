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
import interoperability_py 
import json
import sys

def run_bridge():
    params = {
        "page": "1"
    }

    try:
        json_input = json.dumps(params)
        json_result = interoperability_py.fetch_from_python(json_input)

        data = json.loads(json_result)
        
        print(json.dumps(data, indent=4))

    except Exception as e:
        print(json.dumps({"python_error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    run_bridge()
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
#ramramjiramramjiramramji
#ramramjiramramjuramramji
#ramramjiramramjuramramji