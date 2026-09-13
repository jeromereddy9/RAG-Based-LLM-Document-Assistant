from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType
from src.utils import path_builder

def DocLoader(path,export_type=ExportType.MARKDOWN):
    loader = DoclingLoader(path_builder(path),export_type=export_type)
    return loader.load()

path = "src/data/Proposal speech part.pdf"

doc = DocLoader(path)

print(doc)