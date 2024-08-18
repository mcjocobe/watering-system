{
  lib,
  buildNpmPackage,
  stdenv,
}: let
  build-result = buildNpmPackage {
    pname = "ui";
    version = "1.0.0";

    src = ./.;

    npmDepsHash = "sha256-eQw7dLQgXY9/I6ZUExYcx9kOEzImr3FsDIECn3iV/5A=";
  };
in
  stdenv.mkDerivation {
    name = "water-system-ui";
    src = build-result;

    installPhase = ''
      cp -r lib/node_modules/ui/dist $out/
    '';
  }
