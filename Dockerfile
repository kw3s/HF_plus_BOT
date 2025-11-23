FROM python:3.9-slim

# 1. Create the user first
RUN useradd -m -u 1000 user

# 2. Switch to the user immediately
USER user

# 3. Set the environment so the user can use their own installed apps
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# 4. Set working directory
WORKDIR $HOME/app

# 5. Copy files with correct ownership permissions
COPY --chown=user . $HOME/app

# 6. Install dependencies AS THE USER (This fixes the DNS permission issue)
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 7. Run
CMD ["python", "main.py"]
