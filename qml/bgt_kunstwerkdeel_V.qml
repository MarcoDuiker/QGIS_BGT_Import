<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyAlgorithm="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyLocal="1" simplifyDrawingTol="1" version="3.2.3-Bonn" labelsEnabled="0" readOnly="0" minScale="1e+08" simplifyDrawingHints="1">
  <renderer-v2 symbollevels="0" forceraster="0" type="RuleRenderer" enableorderby="0">
    <rules key="{ed89fb81-1950-4066-a859-1fe6c59134e9}">
      <rule symbol="0" key="{822bcf40-c647-431a-93af-0342487cc414}" label="Gemaal" filter="&quot;bgt-type&quot; = 'gemaal'"/>
      <rule symbol="1" key="{a51873e3-3a10-4b69-aef7-1ea72bf976f5}" label="Hoogspanningsmast" filter="&quot;bgt-type&quot; = 'hoogspanningsmast'" scalemaxdenom="5000"/>
      <rule symbol="2" key="{24a08188-82f1-4515-9fcb-24fbef7931d4}" label="Perron: lijn" filter="&quot;bgt-type&quot; = 'perron'" scalemaxdenom="5000"/>
      <rule symbol="3" key="{cf2f76b2-af93-45ad-b019-aee77fe14c66}" label="Sluis" filter="&quot;bgt-type&quot; = 'sluis'" scalemaxdenom="5000"/>
      <rule symbol="4" key="{fb04b93d-60f9-48a5-9493-d42cb1b86fc9}" label="Steiger" filter="&quot;bgt-type&quot; = 'steiger'" scalemaxdenom="5000"/>
      <rule symbol="5" key="{aa25bdde-6fd7-4ace-9f77-501590fe0710}" label="Strekdam" filter="&quot;bgt-type&quot; = 'strekdam'" scalemaxdenom="5000"/>
      <rule symbol="6" key="{f8ecb862-6162-4240-bbcb-dd3fe2d2c21f}" label="Stuw" filter="&quot;bgt-type&quot; = 'stuw'" scalemaxdenom="5000"/>
      <rule symbol="7" key="{9d602f3c-e279-4b8b-8a57-9ceff4489c83}" label="Bodemval" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'bodemval'" scalemaxdenom="5000"/>
      <rule symbol="8" key="{9a3e3676-1fc4-4028-89d3-34a70aedbb74}" label="Coupure" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'coupure'" scalemaxdenom="5000"/>
      <rule symbol="9" key="{73accd93-4c5c-45e3-9d14-a47d8b26ed7f}" label="Duiker" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'duiker'" scalemaxdenom="5000"/>
      <rule symbol="10" key="{6d393e65-5183-44c5-b384-cd86a3b22a8a}" label="Faunavoorziening" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'faunavoorziening'" scalemaxdenom="5000"/>
      <rule symbol="11" key="{ae940add-ca3e-42ac-8e86-dc02ec06fc5e}" label="Keermuur" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'keermuur'" scalemaxdenom="5000"/>
      <rule symbol="12" key="{9cd22ae3-3491-49d3-8d12-4daa171a308f}" label="Overkluizing" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'overkluizing'" scalemaxdenom="5000"/>
      <rule symbol="13" key="{802bdc98-2c41-47a1-bac0-dd611c0edf29}" label="Ponton" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'ponton'" scalemaxdenom="5000"/>
      <rule symbol="14" key="{60d0ef03-55fb-40e5-9ec7-0203a31897b4}" label="Vispassage" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'vispassage'" scalemaxdenom="5000"/>
      <rule symbol="15" key="{6d851409-a83d-4c40-a99c-634a8a896982}" label="Voorde" filter="&quot;bgt-type&quot; = 'niet-bgt' AND &quot;plus-type&quot; = 'voorde'" scalemaxdenom="5000"/>
      <rule symbol="16" key="{0462cc52-9827-4eca-8f2f-c7d8e0274897}" label="Perron: vulling" filter="&quot;bgt-type&quot; = 'perron'" scalemaxdenom="5000"/>
      <rule symbol="17" key="{35cd9ff3-154c-499f-b284-64f3588b779d}" label="Transitie" filter="&quot;bgt-type&quot; = 'transitie'" scalemaxdenom="5000"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" type="fill" name="0" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="10" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="11" alpha="1">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="0"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="204,0,0,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="2"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" type="fill" name="12" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="13" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="14" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="15" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="16" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,153,153,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="255,153,153,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="17" alpha="1">
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
      <symbol clip_to_extent="1" type="fill" name="2" alpha="1">
        <layer class="SimpleLine" pass="0" enabled="1" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="0"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="Pixel"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="83,83,83,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="3"/>
          <prop k="line_width_unit" v="Pixel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" type="fill" name="3" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="4" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="5" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="6" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="7" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="8" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
      <symbol clip_to_extent="1" type="fill" name="9" alpha="1">
        <layer class="SimpleFill" pass="0" enabled="1" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="204,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="204,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1"/>
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
    <field name="bgt-type">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="plus-type">
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
    <field name="eindRegistratie">
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
    <alias index="12" name="" field="bgt-type"/>
    <alias index="13" name="" field="plus-type"/>
    <alias index="14" name="" field="terminationDate"/>
    <alias index="15" name="" field="eindRegistratie"/>
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
    <default expression="" field="bgt-type" applyOnUpdate="0"/>
    <default expression="" field="plus-type" applyOnUpdate="0"/>
    <default expression="" field="terminationDate" applyOnUpdate="0"/>
    <default expression="" field="eindRegistratie" applyOnUpdate="0"/>
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
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="bgt-type"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="plus-type"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="terminationDate"/>
    <constraint notnull_strength="0" constraints="0" unique_strength="0" exp_strength="0" field="eindRegistratie"/>
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
    <constraint exp="" field="bgt-type" desc=""/>
    <constraint exp="" field="plus-type" desc=""/>
    <constraint exp="" field="terminationDate" desc=""/>
    <constraint exp="" field="eindRegistratie" desc=""/>
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
      <column width="-1" type="field" name="bgt-type" hidden="0"/>
      <column width="-1" type="field" name="plus-type" hidden="0"/>
      <column width="-1" type="field" name="terminationDate" hidden="0"/>
      <column width="-1" type="field" name="eindRegistratie" hidden="0"/>
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
    <field name="bgt-type" editable="1"/>
    <field name="bronhouder" editable="1"/>
    <field name="creationDate" editable="1"/>
    <field name="eindRegistratie" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="gml_id" editable="1"/>
    <field name="inOnderzoek" editable="1"/>
    <field name="lokaalID" editable="1"/>
    <field name="namespace" editable="1"/>
    <field name="plus-status" editable="1"/>
    <field name="plus-type" editable="1"/>
    <field name="relatieveHoogteligging" editable="1"/>
    <field name="terminationDate" editable="1"/>
    <field name="tijdstipRegistratie" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="LV-publicatiedatum"/>
    <field labelOnTop="0" name="bgt-status"/>
    <field labelOnTop="0" name="bgt-type"/>
    <field labelOnTop="0" name="bronhouder"/>
    <field labelOnTop="0" name="creationDate"/>
    <field labelOnTop="0" name="eindRegistratie"/>
    <field labelOnTop="0" name="fid"/>
    <field labelOnTop="0" name="gml_id"/>
    <field labelOnTop="0" name="inOnderzoek"/>
    <field labelOnTop="0" name="lokaalID"/>
    <field labelOnTop="0" name="namespace"/>
    <field labelOnTop="0" name="plus-status"/>
    <field labelOnTop="0" name="plus-type"/>
    <field labelOnTop="0" name="relatieveHoogteligging"/>
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
