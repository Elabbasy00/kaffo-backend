from src.education.selector import EducationRepository


def get_education_stages(*, education_slug: str):
    education = EducationRepository.filter_education_stages(education_stage__slug=education_slug).prefetch_related(
        "grade_levels"
    )
    return education
