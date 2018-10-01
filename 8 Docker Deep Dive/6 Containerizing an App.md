# Containerize an App

## MultiStage Builds

FROM node AS storefront

COPY --from=storefront /usr/src/ .