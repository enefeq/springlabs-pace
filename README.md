# Python client from openapi

springlabs-pace-api.yml provided by SL

# How to generate the openapi client
https://openapi-generator.tech/docs/installation

```
brew install openjdk
yarn
rm -rf ./springlabs-client
npx @openapitools/openapi-generator-cli generate -i springlabs-pace-api.yml -g python -o springlabs-client --additional-properties=packageName=springlabs
```
