FROM python:3.10

WORKDIR /code

# 1. Copy requirements first (efficient caching)
COPY requirements.txt /code/requirements.txt

# 2. Install as ROOT (This ensures global availability of network libraries)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 3. Copy the rest of the code
COPY . .

# 4. Create the user (Hugging Face Standard) and switch permissions
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app
COPY --chown=user . $HOME/app

# 5. Run
CMD ["python", "main.py"]
