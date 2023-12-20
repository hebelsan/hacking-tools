## generate jwts

https://www.scottbrady91.com/tools/jwt

## attacks


### None algorithm

JWT supports a “none” algorithm. If the alg field is set to “none”, any token would be considered valid if their signature section is set to empty. For example, the following token would be considered valid:

*eyAiYWxnIiA6ICJOb25lIiwgInR5cCIgOiAiSldUIiB9Cg.eyB1c2VyX25hbWUgOiBhZG1pbiB9Cg*.

It is simply the base64url encoded versions of these two blobs, and no signature is present.

```json
{
 "alg" : "none",
 "typ" : "JWT"
}
{
 "user" : "admin"
}
```

### HMAC algorithm

The two most common types of algorithms used for JWTs are HMAC and RSA. With HMAC, the token would be signed with a key, then later verified with the same key. As for RSA, the token would first be created with a private key, then verified with the corresponding public key.

Now let’s say that there is an application that was originally designed to use RSA tokens. The tokens are signed with a private key A, which is kept a secret from the public. Then the tokens are verified with public key B, which is available to anyone. This is okay as long as the tokens are always treated as RSA tokens.

```
Token signed with key A -> Token verified with key B (RSA scenario)
```

Now if the attacker changes the alg to HMAC, she might be able to create valid tokens by signing the forged tokens with the RSA public key B.

This is because originally when the token is signed with RSA, the program verifies it with the RSA public key B. When the signing algorithm is switched to HMAC, the token is still verified with the RSA public key B, but this time, the token can be signed with the same public key B (since it’s using HMAC).

```
Token signed with key B -> Token verified with key B (HMAC scenario)
```