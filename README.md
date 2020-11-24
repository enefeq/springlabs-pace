# Generate python client from openapi

# https://openapi-generator.tech/docs/installation

```
brew install openjdk
yarn add @openapitools/openapi-generator-cli
npx @openapitools/openapi-generator-cli generate -i springlabs-pace-api.yml -g python -o springlabs-client --additional-properties=packageName=springlabs
```
