<?xml version="1.0" encoding="UTF-8"?>
<MetaResultFile version="20210114" creator="Solver HFTD - Field 3DFD Monitor">
  <MetaGeometryFile filename="model.gex" lod="1"/>
  <SimulationProperties fieldname="e-field (f=5) [1]" frequency="5" encoded_unit="&amp;U:V^1.:m^-1" quantity="e-field" fieldtype="E-Field" fieldscaling="PEAK" dB_Amplitude="20">
    <SecondaryResults>
      <SecondaryResult name="loss (f=5)_1.rex"/>
      <SecondaryResult name="power (f=5)_1.rex"/>
    </SecondaryResults>
  </SimulationProperties>
  <ResultDataType vector="1" complex="1" timedomain="0" frequencymap="0"/>
  <SimulationDomain min="-74.9827042 -74.9827042 -26.9827042" max="74.9827042 74.9827042 34.1027031"/>
  <PlotSettings Plot="4" ignore_symmetry="0" deformation="0" enforce_culling="0" integer_values="0" default_arrow_type="ARROWS" default_scaling="NONE"/>
  <Source type="SOLVER"/>
  <SpecialMaterials>
    <Background type="NORMAL"/>
    <Material name="Copper (annealed)" type="FIELDFREE"/>
    <Material name="PEC" type="FIELDFREE"/>
  </SpecialMaterials>
  <AuxGeometryFile/>
  <AuxResultFile/>
  <FieldFreeNodes/>
  <SurfaceFieldCoefficients/>
  <UnitCell/>
  <SubVolume/>
  <Units/>
  <ProjectUnits/>
  <TimeSampling/>
  <ResultGroups num_steps="1" transformation="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1" process_mesh_group="0">
    <Frame index="0">
      <FieldResultFile filename="e-field (f=5)_1,1.m3d" type="m3d"/>
    </Frame>
  </ResultGroups>
</MetaResultFile>
