hair_task = """
{
    "tasks": [
        {
            "summary": "Find a hair salon near you",
            "explanation": "To dye your hair we need to find somewhere that offers hair dyes"
        }
    ]
}
"""


# TODO: Create test that mocks out LLM call
# def test_load_task_step_template():
#     try:
#         solve_all_tasks(json.loads(hair_task))
#     except Exception:
#         raise