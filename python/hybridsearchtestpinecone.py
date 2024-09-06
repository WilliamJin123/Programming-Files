from datasets import load_dataset

data = load_dataset("jamescalam/ai-arxiv-chunked", split="train")
data
data = data.map(lambda x: {
    "id": f'{x["id"]}-{x["chunk-id"]}',
    "text": x["chunk"],
    "metadata": {
        "title": x["title"],
        "url": x["source"],
        "primary_category": x["primary_category"],
        "published": x["published"],
        "updated": x["updated"],
        "text": x["chunk"],
    }
})
# drop uneeded columns
data = data.remove_columns([
    "title", "summary", "source",
    "authors", "categories", "comment",
    "journal_ref", "primary_category",
    "published", "updated", "references",
    "doi", "chunk-id",
    "chunk"
])
data
