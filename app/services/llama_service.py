import subprocess
import asyncio

OLLAMA_MODEL = "llama3:8b"

async def get_llama_answer(prompt: str) -> str:
    proc = await asyncio.create_subprocess_exec(
        "ollama", "run", OLLAMA_MODEL, "--prompt", prompt,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"Ollama error: {stderr.decode()}")
    return stdout.decode().strip()
