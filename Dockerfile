FROM python:3.9

# 1. Create the user with ID 1000 (Standard for Hugging Face)
RUN useradd -m -u 1000 user

# 2. Switch to this user immediately
USER user

# 3. Set environment variables so Python knows where to install things
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 4. Set the working directory
WORKDIR $HOME/app

# 5. Copy your files into the container with the correct ownership
COPY --chown=user . $HOME/app

# 6. Install your requirements (as the user, not root)
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 7. Run the application
CMD ["python", "main.py"]
