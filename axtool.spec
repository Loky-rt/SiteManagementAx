extenders:
  - name: service_filehost
    version: 0.1.0
    type: service
    description: "File hosting service with scripted web delivery"
    author: MaorSabag
    min_server_version: "v2.0"
    source: .
    build:
      - go build -buildmode=plugin -o service_filehost.so .
    release:
      globs:
        - "*.so"
        - "ax_config.axs"
        - "config.yaml"
