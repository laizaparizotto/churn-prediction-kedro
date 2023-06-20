"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.10
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_abandono

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_abandono,
                inputs="abandono",
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
            node(
                func=preprocess_abandono,
                inputs="abandono_teste",
                outputs="preprocessed_abandono_teste",
                name="preprocess_abandono_teste_node",
            ),
        ]
    )