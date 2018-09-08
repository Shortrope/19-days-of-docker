# Protecting Secrets

**1. Create the secret**
  - passwords, SSH keys, certificates
  - <= 500K
  - Swarm only
  - Storage is encrypted and replicated in Raft log
  - STDIN or file
  - Define in compose stack file

**2. Grant access to service**
  - docker servcie create --secret X
  - stack compose file - secrets section

**3. App reads secret from /run/secrets/X**
  - in-memory filesystem
  - build commit does not include this directory

Check the Entrypoint or CMD of an image for _FILE or secret

---

If, for example, you are passing a password in an environment variable (like for mysql) then it can  
be viewed with `inspect` or the .yml file!  

But we can create a secret

    docker secret
    docker secret ls
    docker secret create
    echo supersecretpw | docker secret create mysql_root_pw_v1 -
    docker secret rm mysql_root_pass

The '-' means read from STDIN

## Grant a service access to a secret
But this only puts the secret in the file system of the container

    version: '3.7'
    services:
      mysql:
        image: mysql
        environment:
          MYSQL_DATABASE: wordpress
        secrets:
          - mysql_root_pw_v1    # this will NOT work.. it is auto prepended w service name
          - root_pw_v1          # this will work

In the file system of the container, the secret is stored in 

    /run/secrets
Append '_FILE' to an environment var to tell it where to get the value

    version: '3.7'
    services:
      mysql:
        secrets:
          - root_pw_v1
        environment:
          MYSQL_ROOT_PASSWORD_FILE: /run/secrets/root_pw
    
Long form / alias  

      mysql:
        secrets:
          - source: root_pw_v1
            target: root_pw
        environment:
          MYSQL_ROOT_PASSWORD_FILE: /run/secrets/root_pw
With this method you can create a new _vN password and only update the 'source'