<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="1" maxScale="0" simplifyLocal="1" simplifyDrawingTol="1" version="3.2.3-Bonn" labelsEnabled="1" readOnly="0" minScale="2500" simplifyDrawingHints="0">
  <renderer-v2 type="nullSymbol"/>
  <labeling type="simple">
    <settings>
      <text-style fontItalic="0" textOpacity="1" fontUnderline="0" fontStrikeout="0" fontLetterSpacing="0" namedStyle="Normal" fieldName=" regexp_substr( tekst, '[:](-?[^,)]*)[,)]*')" fontSize="0.5" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" multilineHeight="1" fontWeight="50" fontCapitals="0" fontSizeUnit="RenderMetersInMapUnits" blendMode="0" isExpression="1" fontFamily="Sans Serif" useSubstitutions="0" previewBkgrdColor="#ffffff" textColor="0,0,0,255">
        <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferNoFill="1" bufferOpacity="1" bufferBlendMode="0" bufferDraw="0" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferJoinStyle="128" bufferSize="1"/>
        <background shapeRotationType="0" shapeJoinStyle="64" shapeBorderColor="128,128,128,255" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeSVGFile="" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeBlendMode="0" shapeSizeY="0" shapeFillColor="255,255,255,255" shapeSizeType="0" shapeBorderWidth="0" shapeBorderWidthUnit="MM" shapeRadiiY="0" shapeDraw="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeOffsetUnit="MM" shapeRadiiUnit="MM" shapeOpacity="1" shapeRotation="0" shapeOffsetY="0"/>
        <shadow shadowDraw="0" shadowRadiusUnit="MM" shadowColor="0,0,0,255" shadowBlendMode="6" shadowUnder="0" shadowOffsetDist="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetGlobal="1" shadowScale="100" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowOffsetAngle="135" shadowOffsetUnit="MM"/>
        <substitutions/>
      </text-style>
      <text-format rightDirectionSymbol=">" placeDirectionSymbol="0" wrapChar="" decimals="3" reverseDirectionSymbol="0" plussign="0" leftDirectionSymbol="&lt;" formatNumbers="0" multilineAlign="3" addDirectionSymbol="0"/>
      <placement quadOffset="4" maxCurvedCharAngleIn="25" offsetUnits="MM" xOffset="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="0" centroidInside="0" fitInPolygonOnly="0" yOffset="0" distMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" placement="1" maxCurvedCharAngleOut="-25" repeatDistance="0" repeatDistanceUnits="MM" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" offsetType="0" dist="0" priority="5" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" centroidWhole="0" distUnits="MM" rotationAngle="0"/>
      <rendering obstacle="1" maxNumLabels="2000" obstacleType="0" fontLimitPixelSize="0" displayAll="1" obstacleFactor="1" minFeatureSize="0" fontMaxPixelSize="10000" drawLabels="1" scaleVisibility="0" limitNumLabels="0" upsidedownLabels="1" labelPerPart="0" mergeLines="0" scaleMax="0" scaleMin="0" fontMinPixelSize="3" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" type="QString" name="name"/>
          <Option type="Map" name="properties">
            <Option type="Map" name="LabelRotation">
              <Option value="true" type="bool" name="active"/>
              <Option value="to_real( regexp_substr(  &quot;hoek&quot;  , '([-]?\\d+(\\.\\d+)?)[)]'))" type="QString" name="expression"/>
              <Option value="3" type="int" name="type"/>
            </Option>
          </Option>
          <Option value="collection" type="QString" name="type"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="&quot;fid&quot;" key="dualview/previewExpressions"/>
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
  <DiagramLayerSettings dist="0" obstacle="0" zIndex="0" linePlacementFlags="18" placement="0" priority="0" showAll="1">
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
    <field name="identificatieBAGPND">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tekst">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hoek">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identificatieBAGVBOLaagsteHuisnummer">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identificatieBAGVBOHoogsteHuisnummer">
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
    <alias index="12" name="" field="identificatieBAGPND"/>
    <alias index="13" name="" field="tekst"/>
    <alias index="14" name="" field="hoek"/>
    <alias index="15" name="" field="identificatieBAGVBOLaagsteHuisnummer"/>
    <alias index="16" name="" field="identificatieBAGVBOHoogsteHuisnummer"/>
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
    <default expression="" field="identificatieBAGPND" applyOnUpdate="0"/>
    <default expression="" field="tekst" applyOnUpdate="0"/>
    <default expression="" field="hoek" applyOnUpdate="0"/>
    <default expression="" field="identificatieBAGVBOLaagsteHuisnummer" applyOnUpdate="0"/>
    <default expression="" field="identificatieBAGVBOHoogsteHuisnummer" applyOnUpdate="0"/>
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
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="identificatieBAGPND"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="tekst"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="hoek"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="identificatieBAGVBOLaagsteHuisnummer"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="identificatieBAGVBOHoogsteHuisnummer"/>
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
    <constraint exp="" field="identificatieBAGPND" desc=""/>
    <constraint exp="" field="tekst" desc=""/>
    <constraint exp="" field="hoek" desc=""/>
    <constraint exp="" field="identificatieBAGVBOLaagsteHuisnummer" desc=""/>
    <constraint exp="" field="identificatieBAGVBOHoogsteHuisnummer" desc=""/>
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
      <column width="-1" type="field" name="identificatieBAGPND" hidden="0"/>
      <column width="-1" type="field" name="tekst" hidden="0"/>
      <column width="-1" type="field" name="hoek" hidden="0"/>
      <column width="-1" type="field" name="identificatieBAGVBOLaagsteHuisnummer" hidden="0"/>
      <column width="-1" type="field" name="identificatieBAGVBOHoogsteHuisnummer" hidden="0"/>
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
    <field name="gml_id" editable="1"/>
    <field name="hoek" editable="1"/>
    <field name="identificatieBAGPND" editable="1"/>
    <field name="identificatieBAGVBOHoogsteHuisnummer" editable="1"/>
    <field name="identificatieBAGVBOLaagsteHuisnummer" editable="1"/>
    <field name="inOnderzoek" editable="1"/>
    <field name="lokaalID" editable="1"/>
    <field name="namespace" editable="1"/>
    <field name="plus-status" editable="1"/>
    <field name="relatieveHoogteligging" editable="1"/>
    <field name="tekst" editable="1"/>
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
    <field labelOnTop="0" name="gml_id"/>
    <field labelOnTop="0" name="hoek"/>
    <field labelOnTop="0" name="identificatieBAGPND"/>
    <field labelOnTop="0" name="identificatieBAGVBOHoogsteHuisnummer"/>
    <field labelOnTop="0" name="identificatieBAGVBOLaagsteHuisnummer"/>
    <field labelOnTop="0" name="inOnderzoek"/>
    <field labelOnTop="0" name="lokaalID"/>
    <field labelOnTop="0" name="namespace"/>
    <field labelOnTop="0" name="plus-status"/>
    <field labelOnTop="0" name="relatieveHoogteligging"/>
    <field labelOnTop="0" name="tekst"/>
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
  <layerGeometryType>0</layerGeometryType>
</qgis>
