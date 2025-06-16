import subprocess

OLLAMA_MODEL = "llama3:8b"

async def get_llama_answer(prompt: str) -> str:
    proc = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Ollama error: {proc.stderr.decode()}")
    return proc.stdout.decode().strip()
