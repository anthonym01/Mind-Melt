# Mind-Melt
Mind Melt (MM) llm programing language

## Dependencies  

- ply
- venv
- Flask

## How to run

### Settup Linux/Mac
run
```sh
cd Yourkoza2 ; python3 -m venv .venv ; . .venv/bin/activate ; pip install Flask ; pip install ply ; pip install pylance; pip install -q -U google-generativeai; pip install python-dotenv;
```

### Settup Windows
run
```bash
cd Yourkoza2 ; py -3 -m venv .venv ; .venv\Scripts\activate ; pip install Flask ; pip install ply ; pip install Flask ; pip install ply ; pip install pylance; pip install -q -U google-generativeai; pip install python-dotenv;
```

afterwards run:

```python
flask --app yourkoza run --host=0.0.0.0 --debug --port=8080
```
