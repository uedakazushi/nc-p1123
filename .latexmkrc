# Build papers/nc-p1123.tex from the repository root or in VS Code.
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$max_repeat = 5;
$out_dir = '.';
$clean_ext .= ' synctex.gz';

# With no explicit filename, latexmk should select the main paper.
@default_files = ('papers/nc-p1123.tex');
