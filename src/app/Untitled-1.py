print("Hello AI World! My journey to $100M starts here.")
from transformers import pipeline

summarizer = pipeline("summarization")
TEXT = """Artificial Intelligence (AI) and Machine Learning (ML) are transforming industries by automating
tasks, improving decision making, and enabling new products and services. Businesses use AI chatbots,
recommendation systems, fraud detection, and more to save time and increase profits."""

print(summarizer(TEXT, max_length=50, min_length=25, do_sample=False))
from transformers import pipeline

# Load summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Text to summarize
TEXT = """Artificial Intelligence (AI) and Machine Learning (ML) are transforming industries by automating
tasks, improving decision making, and enabling new products and services. Businesses use AI chatbots,
recommendation systems, fraud detection, and more to save time and increase profits."""

# Run summarizer
summary = summarizer(TEXT, max_length=50, min_length=25, do_sample=False)

# Print result
print("Summary:", summary[0]['summary_text'])

