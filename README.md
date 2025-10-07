# Vulnerable Web Application

**WARNING: This is a deliberately vulnerable web application created for educational purposes. DO NOT deploy this in a production environment or expose it to the internet.**

## Description

This is a deliberately vulnerable Flask web application designed for learning about common web security vulnerabilities in a safe, controlled environment. It includes several intentional security flaws that you can explore and exploit to learn about web security.

## Vulnerabilities

This application includes several common vulnerabilities:

1. SQL Injection
2. Cross-Site Scripting (XSS)
3. Command Injection
4. Weak Password Storage
5. No CSRF Protection

## Setup

### Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t vuln-webapp .
```

2. Run the container:
```bash
docker run -p 5000:5000 vuln-webapp
```

The application will be available at http://localhost:5000

### Manual Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Security Testing Exercises

### 1. SQL Injection
Try to:
- Login without knowing the password
- Extract user data from the database
Example payloads:
- Username: `admin' --`
- Username: `' OR '1'='1`

### 2. XSS (Cross-Site Scripting)
Try to:
- Inject JavaScript in the dashboard page
- Steal session cookies
Example payload:
- `<script>alert('XSS')</script>`

### 3. Command Injection
Try to:
- Execute system commands through the search feature
Example payloads:
- `test; ls`
- `test && cat /etc/passwd`

## Disclaimer

This application is for educational purposes only. Always:
1. Get proper authorization before testing real systems
2. Only test systems you own or have explicit permission to test
3. Practice responsible disclosure
4. Never use these techniques against real websites without permission

## License

MIT License

## Contributing

Feel free to submit issues and enhancement requests!