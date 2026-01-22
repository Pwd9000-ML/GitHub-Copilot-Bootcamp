# Security Guidelines

This document provides security guidelines for developing secure applications with GitHub Copilot assistance.

## Security First Mindset

- Assume all input is malicious
- Apply defense in depth
- Follow principle of least privilege
- Keep security simple
- Fail securely

## OWASP Top 10 (2021)

### 1. Broken Access Control
**Risk**: Users acting outside intended permissions

**Prevention**:
- Implement proper authorization checks
- Deny by default
- Validate permissions server-side
- Use role-based access control (RBAC)

**Example (TypeScript)**:
```typescript
// Good
async function deleteUser(userId: string, requesterId: string): Promise<void> {
  const requester = await userService.getUser(requesterId);
  
  if (!requester.hasRole('admin')) {
    throw new UnauthorizedError('Only admins can delete users');
  }
  
  await userService.delete(userId);
}

// Avoid - No authorization check
async function deleteUser(userId: string): Promise<void> {
  await userService.delete(userId);
}
```

### 2. Cryptographic Failures
**Risk**: Exposure of sensitive data

**Prevention**:
- Encrypt data at rest and in transit
- Use strong, modern cryptographic algorithms
- Properly manage cryptographic keys
- Use TLS/SSL for all communications

**Example (Node.js)**:
```typescript
import { createCipheriv, randomBytes, scrypt } from 'crypto';

// Good - Proper encryption
async function encryptData(data: string, password: string): Promise<string> {
  const salt = randomBytes(16);
  const key = await scrypt(password, salt, 32);
  const iv = randomBytes(16);
  const cipher = createCipheriv('aes-256-gcm', key, iv);
  
  const encrypted = Buffer.concat([
    cipher.update(data, 'utf8'),
    cipher.final()
  ]);
  
  return `${salt.toString('hex')}:${iv.toString('hex')}:${encrypted.toString('hex')}`;
}

// Avoid - Weak encryption
function encryptData(data: string): string {
  return Buffer.from(data).toString('base64'); // Not encryption!
}
```

### 3. Injection
**Risk**: Untrusted data sent to interpreter

**Prevention**:
- Use parameterized queries
- Validate and sanitize input
- Use ORM/query builders
- Escape special characters

**Example (Python)**:
```python
# Good - Parameterized query
def get_user_by_email(email: str) -> User:
    query = "SELECT * FROM users WHERE email = ?"
    return db.execute(query, (email,)).fetchone()

# Avoid - SQL Injection vulnerable
def get_user_by_email(email: str) -> User:
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return db.execute(query).fetchone()
```

**Example (JavaScript)**:
```javascript
// Good - Use query builder
const user = await db('users')
  .where('email', email)
  .first();

// Avoid - String concatenation
const query = `SELECT * FROM users WHERE email = '${email}'`;
const user = await db.raw(query);
```

### 4. Insecure Design
**Risk**: Missing or ineffective security controls

**Prevention**:
- Threat modeling
- Security requirements
- Secure design patterns
- Security reviews

### 5. Security Misconfiguration
**Risk**: Insecure default configurations

**Prevention**:
- Remove default accounts
- Disable unnecessary features
- Keep software updated
- Use security headers

**Example (Express.js)**:
```typescript
import helmet from 'helmet';

// Good - Security headers
app.use(helmet());
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    scriptSrc: ["'self'"]
  }
}));

app.disable('x-powered-by');
```

### 6. Vulnerable and Outdated Components
**Risk**: Using components with known vulnerabilities

**Prevention**:
- Keep dependencies updated
- Use dependency scanning (Dependabot)
- Remove unused dependencies
- Monitor security advisories

**Commands**:
```bash
# Check for vulnerabilities
npm audit
pip-audit
```

### 7. Identification and Authentication Failures
**Risk**: Broken authentication mechanisms

**Prevention**:
- Implement multi-factor authentication
- Use strong password policies
- Protect against brute force attacks
- Secure session management

**Example (Node.js)**:
```typescript
import bcrypt from 'bcrypt';

// Good - Secure password hashing
async function hashPassword(password: string): Promise<string> {
  const saltRounds = 12;
  return bcrypt.hash(password, saltRounds);
}

async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash);
}

// Avoid - Plain text or weak hashing
function hashPassword(password: string): string {
  return crypto.createHash('md5').update(password).digest('hex'); // Weak!
}
```

### 8. Software and Data Integrity Failures
**Risk**: Unverified software or data updates

**Prevention**:
- Use digital signatures
- Verify package integrity
- Implement CI/CD security
- Use trusted repositories

### 9. Security Logging and Monitoring Failures
**Risk**: Insufficient logging and monitoring

**Prevention**:
- Log security events
- Implement alerting
- Regular log review
- Centralized logging

**Example (TypeScript)**:
```typescript
import logger from './logger';

// Good - Log security events
async function login(username: string, password: string): Promise<User> {
  try {
    const user = await authenticateUser(username, password);
    logger.info('Successful login', { username, userId: user.id });
    return user;
  } catch (error) {
    logger.warn('Failed login attempt', { username, ip: request.ip });
    throw new AuthenticationError('Invalid credentials');
  }
}
```

### 10. Server-Side Request Forgery (SSRF)
**Risk**: Application fetches remote resources without validation

**Prevention**:
- Validate and sanitize URLs
- Use allow lists
- Disable unnecessary protocols
- Network segmentation

**Example (Python)**:
```python
from urllib.parse import urlparse

# Good - URL validation
ALLOWED_DOMAINS = ['api.example.com', 'cdn.example.com']

def fetch_resource(url: str) -> bytes:
    parsed = urlparse(url)
    
    if parsed.hostname not in ALLOWED_DOMAINS:
        raise ValueError('Domain not allowed')
    
    if parsed.scheme not in ['https']:
        raise ValueError('Only HTTPS allowed')
    
    return requests.get(url).content

# Avoid - No validation
def fetch_resource(url: str) -> bytes:
    return requests.get(url).content
```

## Input Validation

### Always Validate Input
- Validate on server-side (never trust client)
- Use allowlists over denylists
- Validate type, length, format, range
- Sanitize for context (HTML, SQL, etc.)

**Example (TypeScript)**:
```typescript
import { z } from 'zod';

// Good - Schema validation
const userSchema = z.object({
  email: z.string().email().max(255),
  age: z.number().int().min(18).max(120),
  username: z.string().min(3).max(30).regex(/^[a-zA-Z0-9_]+$/)
});

function createUser(data: unknown): User {
  const validated = userSchema.parse(data);
  return userService.create(validated);
}
```

## Authentication & Authorization

### Secure Authentication
- Use established auth protocols (OAuth2, OpenID Connect)
- Implement rate limiting
- Use secure session management
- Implement account lockout

### Authorization
- Check permissions on every request
- Use RBAC or ABAC
- Principle of least privilege
- Separate authentication from authorization

## Secrets Management

### Never Commit Secrets
- Use environment variables
- Use secret management tools (Vault, AWS Secrets Manager)
- Rotate secrets regularly
- Use different secrets per environment

**Example (.env)**:
```bash
# Good - Environment variables
DATABASE_URL=postgresql://...
API_KEY=your-secret-key
JWT_SECRET=random-secret

# Never commit this file!
```

## Cross-Site Scripting (XSS) Prevention

### Output Encoding
- Encode output for context (HTML, JavaScript, CSS, URL)
- Use framework protections (React auto-escapes)
- Set Content-Security-Policy header
- Validate input

**Example (React)**:
```typescript
// Good - React auto-escapes
function UserProfile({ username }: Props) {
  return <div>Hello, {username}!</div>;
}

// Dangerous - Manual HTML
function UserProfile({ username }: Props) {
  return <div dangerouslySetInnerHTML={{ __html: username }} />; // Avoid!
}
```

## Cross-Site Request Forgery (CSRF) Prevention

- Use CSRF tokens
- SameSite cookie attribute
- Verify origin/referer headers
- Double submit cookies

**Example (Express.js)**:
```typescript
import csrf from 'csurf';

// Good - CSRF protection
const csrfProtection = csrf({ cookie: true });
app.use(csrfProtection);

app.get('/form', (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});
```

## API Security

### REST API Security
- Use HTTPS only
- Implement authentication (JWT, OAuth2)
- Rate limiting
- Input validation
- Version APIs

### Rate Limiting
```typescript
import rateLimit from 'express-rate-limit';

// Good - Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);
```

## Security Testing

### Automated Testing
- Include security test cases
- Test authentication/authorization
- Test input validation
- Fuzz testing

### Tools
- OWASP ZAP
- Burp Suite
- Snyk
- GitHub Code Scanning
- Dependabot

## Secure Coding with Copilot

### Review Generated Code
- Always review security implications
- Don't trust generated code blindly
- Test security aspects
- Verify authentication/authorization

### Prompt for Security
```typescript
// Prompt Copilot with security requirements
// Create a secure password reset endpoint with:
// - Rate limiting
// - Token expiration
// - Email verification
// - Secure token generation
```

## Incident Response

### If Security Issue Found
1. Assess severity and impact
2. Contain the issue
3. Fix the vulnerability
4. Deploy the fix
5. Post-mortem analysis
6. Update procedures

## Compliance

### Data Protection
- GDPR compliance (if applicable)
- Data minimization
- Right to deletion
- Consent management
- Privacy by design

### PCI DSS (if handling payments)
- Never store CVV
- Encrypt card data
- Use PCI-compliant payment processors
- Regular security testing

## Security Checklist

Before deploying:
- [ ] All inputs validated
- [ ] SQL injection prevented
- [ ] XSS prevention implemented
- [ ] CSRF protection enabled
- [ ] Authentication required
- [ ] Authorization checked
- [ ] Secrets not in code
- [ ] Dependencies updated
- [ ] Security headers set
- [ ] HTTPS enforced
- [ ] Logging implemented
- [ ] Error messages don't leak info

## Resources

- [OWASP](https://owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [GitHub Security](https://docs.github.com/en/code-security)

---

Security is everyone's responsibility. When in doubt, ask the security team!
