\NeedsTeXFormat{LaTeX2e} % Specify the required LaTeX format
\ProvidesClass{LnxClase}[2025/03/18 Plantilla personalizada] % Define the class name and version info

% Load the base class
\LoadClass[a4paper]{article} % Use the 'article' class with A4 paper size

% Load required packages
\RequirePackage[utf8]{inputenc} % Enable UTF-8 encoding
\RequirePackage[spanish]{babel} % Set the language to Spanish
\RequirePackage{amsmath, amssymb, physics} % Load math and physics packages
\RequirePackage{tikz} % Load TikZ for graphics
\RequirePackage{geometry} % Load geometry package for page layout
\RequirePackage{Lnx} % Custom package (assumed to be specific to this template)

% Set custom page size and margins
\geometry{papersize={21cm,32cm}, top=1in, left=1.4cm, right=1.4cm, bottom=1in, includefoot}

\endinput % End of the class file