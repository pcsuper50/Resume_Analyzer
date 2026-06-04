from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load lightweight model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_ats_score(resume_text, job_description):

    # Generate embeddings
    resume_embedding = model.encode(resume_text)

    jd_embedding = model.encode(job_description)

    # Calculate similarity
    similarity_score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    ats_score = round(similarity_score * 100, 2)

    return ats_score