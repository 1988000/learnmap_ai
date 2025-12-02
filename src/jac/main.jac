walker learn_map {
    can start;

    has concept = "Introduction to AI";
    has related = ["Machine Learning", "Neural Networks", "Deep Learning"];

    start() -> report start {
        return {
            "concept": concept,
            "related": related
        };
    }
}
