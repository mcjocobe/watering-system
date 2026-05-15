{pkgs}: let
  python = pkgs.python311.withPackages (ps:
    with ps; [
      docker
      uvicorn
      pytest
    ]);
  default = pkgs.mkShell {
    packages = with pkgs; [
      alejandra
      black
      cmake
      firebase-tools
      git
      gcc
      nodejs
      nodejs_20
      nodePackages.prettier
      npm-check-updates
      pgformatter
      prefetch-npm-deps
      python
    ];
    shellHook = ''npm install src/ui/watering-system/'';
  };
in {
  inherit default;
}
