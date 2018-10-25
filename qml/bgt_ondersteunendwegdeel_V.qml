<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyLocal="1" simplifyDrawingTol="1" version="3.2.3-Bonn" labelsEnabled="0" readOnly="0" minScale="1e+08" simplifyDrawingHints="1">
  <renderer-v2 symbollevels="0" forceraster="0" type="RuleRenderer" enableorderby="0">
    <rules key="{cd52b2fc-f732-4b43-84d5-c5f95aab8c3c}">
      <rule symbol="0" key="{ad0970bc-8f2b-492e-a759-ec146d06b33e}" label="Berm" filter="&quot;function&quot; = 'berm'"/>
      <rule symbol="1" key="{d94430e2-4e0e-4f7f-a378-e51461b3e1c8}" label="Verkeerseiland" filter="&quot;function&quot; = 'verkeerseiland'"/>
      <rule symbol="2" key="{9e26c61d-91f8-46df-ab38-58242d8a630a}" label="Transitie" filter="&quot;function&quot; = 'transitie'"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" type="fill" name="0" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,153,153,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,153,153,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="2"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" type="fill" name="1" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,153,153,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,153,153,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="2"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" type="fill" name="2" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="242,242,242,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="83,83,83,255"/>
          <prop k="outline_style" v="dash"/>
          <prop k="outline_width" v="2"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property value="fid" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory penWidth="0" backgroundAlpha="255" penAlpha="255" backgroundColor="#ffffff" lineSizeType="MM" scaleDependency="Area" height="15" rotationOffset="270" minScaleDenominator="0" width="15" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" sizeType="MM" barWidth="5" diagramOrientation="Up" sizeScale="3x:0,0,0,0,0,0" penColor="#000000" enabled="0" opacity="1" labelPlacementMethod="XHeight" maxScaleDenominator="1e+08" minimumSize="0">
      <fontProperties description="Sans Serif,9,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" field="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" obstacle="0" zIndex="0" linePlacementFlags="18" placement="1" priority="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gml_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="creationDate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="LV-publicatiedatum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="relatieveHoogteligging">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="inOnderzoek">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tijdstipRegistratie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="namespace">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lokaalID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="bronhouder">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="bgt-status">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plus-status">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="function">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="surfaceMaterial">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ondersteunendWegdeelOpTalud">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plus-functieOndersteunendWegdeel">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plus-fysiekVoorkomenOndersteunendWegdeel">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eindRegistratie">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="terminationDate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="fid"/>
    <alias index="1" name="" field="gml_id"/>
    <alias index="2" name="" field="creationDate"/>
    <alias index="3" name="" field="LV-publicatiedatum"/>
    <alias index="4" name="" field="relatieveHoogteligging"/>
    <alias index="5" name="" field="inOnderzoek"/>
    <alias index="6" name="" field="tijdstipRegistratie"/>
    <alias index="7" name="" field="namespace"/>
    <alias index="8" name="" field="lokaalID"/>
    <alias index="9" name="" field="bronhouder"/>
    <alias index="10" name="" field="bgt-status"/>
    <alias index="11" name="" field="plus-status"/>
    <alias index="12" name="" field="function"/>
    <alias index="13" name="" field="surfaceMaterial"/>
    <alias index="14" name="" field="ondersteunendWegdeelOpTalud"/>
    <alias index="15" name="" field="plus-functieOndersteunendWegdeel"/>
    <alias index="16" name="" field="plus-fysiekVoorkomenOndersteunendWegdeel"/>
    <alias index="17" name="" field="eindRegistratie"/>
    <alias index="18" name="" field="terminationDate"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="fid" applyOnUpdate="0"/>
    <default expression="" field="gml_id" applyOnUpdate="0"/>
    <default expression="" field="creationDate" applyOnUpdate="0"/>
    <default expression="" field="LV-publicatiedatum" applyOnUpdate="0"/>
    <default expression="" field="relatieveHoogteligging" applyOnUpdate="0"/>
    <default expression="" field="inOnderzoek" applyOnUpdate="0"/>
    <default expression="" field="tijdstipRegistratie" applyOnUpdate="0"/>
    <default expression="" field="namespace" applyOnUpdate="0"/>
    <default expression="" field="lokaalID" applyOnUpdate="0"/>
    <default expression="" field="bronhouder" applyOnUpdate="0"/>
    <default expression="" field="bgt-status" applyOnUpdate="0"/>
    <default expression="" field="plus-status" applyOnUpdate="0"/>
    <default expression="" field="function" applyOnUpdate="0"/>
    <default expression="" field="surfaceMaterial" applyOnUpdate="0"/>
    <default expression="" field="ondersteunendWegdeelOpTalud" applyOnUpdate="0"/>
    <default expression="" field="plus-functieOndersteunendWegdeel" applyOnUpdate="0"/>
    <default expression="" field="plus-fysiekVoorkomenOndersteunendWegdeel" applyOnUpdate="0"/>
    <default expression="" field="eindRegistratie" applyOnUpdate="0"/>
    <default expression="" field="terminationDate" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" constraints="3" unique_strength="1" exp_strength="0" field="fid"/>
    <constraint notnull_strength="1" constraints="1" unique_strength="0" exp_strength="0" field="gml_id"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="creationDate"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="LV-publicatiedatum"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="relatieveHoogteligging"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="inOnderzoek"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="tijdstipRegistratie"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="namespace"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="lokaalID"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="bronhouder"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="bgt-status"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="plus-status"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="function"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="surfaceMaterial"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="ondersteunendWegdeelOpTalud"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="plus-functieOndersteunendWegdeel"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="plus-fysiekVoorkomenOndersteunendWegdeel"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="eindRegistratie"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="terminationDate"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="fid" desc=""/>
    <constraint exp="" field="gml_id" desc=""/>
    <constraint exp="" field="creationDate" desc=""/>
    <constraint exp="" field="LV-publicatiedatum" desc=""/>
    <constraint exp="" field="relatieveHoogteligging" desc=""/>
    <constraint exp="" field="inOnderzoek" desc=""/>
    <constraint exp="" field="tijdstipRegistratie" desc=""/>
    <constraint exp="" field="namespace" desc=""/>
    <constraint exp="" field="lokaalID" desc=""/>
    <constraint exp="" field="bronhouder" desc=""/>
    <constraint exp="" field="bgt-status" desc=""/>
    <constraint exp="" field="plus-status" desc=""/>
    <constraint exp="" field="function" desc=""/>
    <constraint exp="" field="surfaceMaterial" desc=""/>
    <constraint exp="" field="ondersteunendWegdeelOpTalud" desc=""/>
    <constraint exp="" field="plus-functieOndersteunendWegdeel" desc=""/>
    <constraint exp="" field="plus-fysiekVoorkomenOndersteunendWegdeel" desc=""/>
    <constraint exp="" field="eindRegistratie" desc=""/>
    <constraint exp="" field="terminationDate" desc=""/>
  </constraintExpressions>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" type="field" name="fid" hidden="0"/>
      <column width="-1" type="field" name="gml_id" hidden="0"/>
      <column width="-1" type="field" name="creationDate" hidden="0"/>
      <column width="-1" type="field" name="LV-publicatiedatum" hidden="0"/>
      <column width="-1" type="field" name="relatieveHoogteligging" hidden="0"/>
      <column width="-1" type="field" name="inOnderzoek" hidden="0"/>
      <column width="-1" type="field" name="tijdstipRegistratie" hidden="0"/>
      <column width="-1" type="field" name="namespace" hidden="0"/>
      <column width="-1" type="field" name="lokaalID" hidden="0"/>
      <column width="-1" type="field" name="bronhouder" hidden="0"/>
      <column width="-1" type="field" name="bgt-status" hidden="0"/>
      <column width="-1" type="field" name="plus-status" hidden="0"/>
      <column width="-1" type="field" name="function" hidden="0"/>
      <column width="-1" type="field" name="surfaceMaterial" hidden="0"/>
      <column width="-1" type="field" name="ondersteunendWegdeelOpTalud" hidden="0"/>
      <column width="-1" type="field" name="plus-functieOndersteunendWegdeel" hidden="0"/>
      <column width="286" type="field" name="plus-fysiekVoorkomenOndersteunendWegdeel" hidden="0"/>
      <column width="-1" type="field" name="eindRegistratie" hidden="0"/>
      <column width="-1" type="field" name="terminationDate" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
    </columns>
  </attributetableconfig>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Formulieren van QGIS kunnen een functie voor Python hebben die wordt aangeroepen wanneer het formulier wordt geopend.

Gebruik deze functie om extra logica aan uw formulieren toe te voegen.

Voer de naam van de functie in in het veld "Python Init function".

Een voorbeeld volgt hieronder:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="LV-publicatiedatum" editable="1"/>
    <field name="bgt-status" editable="1"/>
    <field name="bronhouder" editable="1"/>
    <field name="creationDate" editable="1"/>
    <field name="eindRegistratie" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="function" editable="1"/>
    <field name="gml_id" editable="1"/>
    <field name="inOnderzoek" editable="1"/>
    <field name="lokaalID" editable="1"/>
    <field name="namespace" editable="1"/>
    <field name="ondersteunendWegdeelOpTalud" editable="1"/>
    <field name="plus-functieOndersteunendWegdeel" editable="1"/>
    <field name="plus-fysiekVoorkomenOndersteunendWegdeel" editable="1"/>
    <field name="plus-status" editable="1"/>
    <field name="relatieveHoogteligging" editable="1"/>
    <field name="surfaceMaterial" editable="1"/>
    <field name="terminationDate" editable="1"/>
    <field name="tijdstipRegistratie" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="LV-publicatiedatum"/>
    <field labelOnTop="0" name="bgt-status"/>
    <field labelOnTop="0" name="bronhouder"/>
    <field labelOnTop="0" name="creationDate"/>
    <field labelOnTop="0" name="eindRegistratie"/>
    <field labelOnTop="0" name="fid"/>
    <field labelOnTop="0" name="function"/>
    <field labelOnTop="0" name="gml_id"/>
    <field labelOnTop="0" name="inOnderzoek"/>
    <field labelOnTop="0" name="lokaalID"/>
    <field labelOnTop="0" name="namespace"/>
    <field labelOnTop="0" name="ondersteunendWegdeelOpTalud"/>
    <field labelOnTop="0" name="plus-functieOndersteunendWegdeel"/>
    <field labelOnTop="0" name="plus-fysiekVoorkomenOndersteunendWegdeel"/>
    <field labelOnTop="0" name="plus-status"/>
    <field labelOnTop="0" name="relatieveHoogteligging"/>
    <field labelOnTop="0" name="surfaceMaterial"/>
    <field labelOnTop="0" name="terminationDate"/>
    <field labelOnTop="0" name="tijdstipRegistratie"/>
  </labelOnTop>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <expressionfields/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
