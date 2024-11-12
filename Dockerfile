FROM python:3-alpine AS builder

WORKDIR /app

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2
FROM python:3-alpine AS runner

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

WORKDIR /app

COPY --from=builder /app /app

# Copia el script de entrada
COPY entrypoint.sh /entrypoint.sh

# Haz que el script de entrada sea ejecutable
RUN chmod +x /entrypoint.sh

EXPOSE ${PORT}

# Usa el script de entrada
ENTRYPOINT ["/entrypoint.sh"]