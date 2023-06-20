"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.10
"""
from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, test_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="classifier",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
            ),
            node(
                func=test_model,
                inputs=["classifier", "preprocessed_abandono_teste"],
                outputs="resultado_teste",
                name="test_model_node",
            ),
        ]
    )