load("//build_defs:defaults.bzl", "ANGULAR_CDK_TS_DEPS", "ANGULAR_CORE_DEPS", "ANGULAR_MATERIAL_TS_DEPS", "ng_module", "sass_binary")

package(
    default_visibility = ["//build_defs:mesop_internal"],
)

ng_module(
    name = "component_tree",
    srcs = glob([
        "*.ts",
    ]),
    assets = glob([
        "*.ng.html",
    ]) + [":component_tree.css"],
    deps = [
        "//mesop/protos:ui_jspb_proto",
        "//mesop/web/src/component_renderer",
        "//mesop/web/src/dev_tools/services",
        "//mesop/web/src/services",
        "//mesop/web/src/utils",
    ] + ANGULAR_CORE_DEPS + ANGULAR_MATERIAL_TS_DEPS + ANGULAR_CDK_TS_DEPS,
)

sass_binary(
    name = "styles",
    src = "component_tree.scss",
    sourcemap = False,
)
