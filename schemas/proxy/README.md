## 📝 Proxy Schema

This package publishes the latest ThreatCode Proxy API schema artifacts so tools can consume a stable, versioned source of truth for GraphQL and OpenAPI definitions.

### Included files

- `schema.graphql`
- `openapi.yaml`

### Install

Using npm:

```bash
npm install @threatcode/schema-proxy
```

Using Python:

```bash
uv add threatcode-schema-proxy
```

### Usage

#### Node.js

```js
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const graphqlSchemaPath = require.resolve("@threatcode/schema-proxy/graphql");
const openApiSchemaPath = require.resolve("@threatcode/schema-proxy/openapi");

const graphqlSchema = readFileSync(graphqlSchemaPath, "utf8");
const openApiSchema = readFileSync(openApiSchemaPath, "utf8");

console.log(graphqlSchema.slice(0, 120));
console.log(openApiSchema.slice(0, 120));
```

#### Python

```python
from importlib import resources

graphql_schema = resources.files("threatcode_schema_proxy").joinpath("schema.graphql").read_text()
openapi_schema = resources.files("threatcode_schema_proxy").joinpath("openapi.yaml").read_text()

print(graphql_schema[:120])
print(openapi_schema[:120])
```

The package exports the current schema files directly for tooling that needs to fetch or validate the Proxy API contract.
