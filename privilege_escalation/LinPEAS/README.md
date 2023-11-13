- winPEAS binaries are in https://www.kali.org/tools/peass-ng/

- https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | ssh emily@10.10.11.219 'cat > linpeas.sh'
```

- always add -a (all checks) option to don't miss thing like cronjobs which run every minute
