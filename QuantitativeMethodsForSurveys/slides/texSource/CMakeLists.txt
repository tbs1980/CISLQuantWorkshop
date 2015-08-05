cmake_minimum_required(VERSION 2.8)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

project(STBalanQuantsForSurveys NONE)
include(${CMAKE_SOURCE_DIR}/cmake/UseLATEX.cmake)

set(PDFLATEX_COMPILER xelatex)
set(PDFLATEX_COMPILER_FLAGS  "--shell-escape")

add_latex_document(STBalanQuantsForSurveys.tex
    #INPUTS src/source1.tex
    #BIBFILES bib/latexCMake.bib
    IMAGE_DIRS img
    DEFAULT_PDF)
