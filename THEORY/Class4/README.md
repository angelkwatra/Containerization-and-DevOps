# Class 4 -- Interacting with the Docker Engine API

## Objective

-   Understand how to interact directly with the Docker Daemon bypassing the Docker CLI.
-   Learn to execute commands against the Docker Engine API using `curl` and the Unix socket (`/var/run/docker.sock`).
-   Perform container lifecycle operations (create, start, stop, restart, inspect) via HTTP API requests.

------------------------------------------------------------------------

## Environment Used

-   Host OS: macOS (Apple Silicon)
-   Container Platform: Docker Desktop
-   Access to the Docker socket at `/var/run/docker.sock`

------------------------------------------------------------------------

## Experiment Execution with Screenshots

### 🔹 Step 1: Retrieve Image Information

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.44/images/json
```

![Step 1 -- Image Information](0.png)

------------------------------------------------------------------------

### 🔹 Step 2: Retrieve All Containers

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.44/containers/json?all=true
```

![Step 2 -- All Containers](1.png)

------------------------------------------------------------------------

### 🔹 Step 3: Create a Container (POST Request - Part 1)

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock \
-H "Content-Type: application/json" \
-d '{"Image": "nginx:latest", "ExposedPorts": {"80/tcp": {}}, "HostConfig": {"PortBindings": {"80/tcp": [{"HostPort": "8080"}]}}}' \
-X POST http://localhost/v1.44/containers/create?name=mynginx
```

![Step 3 -- Create Container Input 1](2.png)

------------------------------------------------------------------------

### 🔹 Step 4: Create a Container (POST Request - Part 2)

**Viewing the multi-line curl command completion:**

![Step 4 -- Create Container Input 2](3.png)

------------------------------------------------------------------------

### 🔹 Step 5: Container Creation Output

**Returned JSON response from the Daemon:**

![Step 5 -- Container ID Response](4.png)

------------------------------------------------------------------------

### 🔹 Step 6: Start the Container

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock -X POST http://localhost/v1.44/containers/mynginx/start
```

![Step 6 -- Start Container Command](5.png)

------------------------------------------------------------------------

### 🔹 Step 7: Start Container Result

**Viewing the empty successful output from the daemon.**

![Step 7 -- Start Container Output](6.png)

------------------------------------------------------------------------

### 🔹 Step 8: Inspect the Container (Running State)

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.44/containers/mynginx/json
```

![Step 8 -- Running Output Payload](7.png)

------------------------------------------------------------------------

### 🔹 Step 9: Stop the Container

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock -X POST http://localhost/v1.44/containers/mynginx/stop
```

![Step 9 -- Stop Container Output](8.png)

------------------------------------------------------------------------

### 🔹 Step 10: Inspect the Container (Stopped State)

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.44/containers/mynginx/json
```

![Step 10 -- Stopped Output Payload](9.png)

------------------------------------------------------------------------

### 🔹 Step 11: Restart the Container

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock \
-X POST \
http://localhost/v1.44/containers/mynginx/restart
```

![Step 11 -- Restart Container Command](10.png)

------------------------------------------------------------------------

### 🔹 Step 12: Verify the Restarted State

**Command executed:**

``` bash
curl --unix-socket /var/run/docker.sock http://localhost/v1.44/containers/mynginx/json
```

![Step 12 -- Restarted Output Payload](11.png)

------------------------------------------------------------------------

## Result

-   Successfully interacted with the Docker Daemon directly via its socket, proving that the `docker` CLI simply wraps these HTTP API calls.
-   Completed full container lifecycle operations natively with `curl` API bindings.
