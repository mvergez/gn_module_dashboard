"""
   Spécification du schéma toml des paramètres de configurations
   Fichier spécifiant les types des paramètres et leurs valeurs par défaut
   Fichier à ne pas modifier. Paramètres surcouchables dans config/config_gn_module.tml
"""

from marshmallow import Schema, fields, validates_schema, ValidationError


class GnModuleSchemaConf(Schema):
    AREA_TYPE = fields.List(fields.String(), missing=["COM", "M1", "M5", "M10"])
    BORNE_TAXON = fields.List(fields.Integer(), missing=[100, 200, 300, 400, 500, 600])
    BORNE_OBS = fields.List(
        fields.Integer(), missing=[1, 1000, 2000, 3000, 4000, 5000, 10000]
    )

