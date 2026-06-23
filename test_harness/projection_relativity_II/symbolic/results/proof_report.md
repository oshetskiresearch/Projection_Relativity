# Projection Relativity II Maple Proof Report

Each entry records the proof method and residual/result for a passing assertion.

## G001 - [T1,T2]=iT3

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: matrix
- actual: `Matrix(2, 2, [[.500000000000000000*I,0.],[0.,-.500000000000000000*I]])`
- expected: `Matrix(2, 2, [[.500000000000000000*I,0.],[0.,-.500000000000000000*I]])`
- residual_or_error: `0.`
- tolerance: `0.`

## G002 - [T2,T3]=iT1

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: matrix
- actual: `Matrix(2, 2, [[0.,.500000000000000000*I],[.500000000000000000*I,0.]])`
- expected: `Matrix(2, 2, [[0.,.500000000000000000*I],[.500000000000000000*I,0.]])`
- residual_or_error: `0.`
- tolerance: `0.`

## G003 - [T3,T1]=iT2

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: matrix
- actual: `Matrix(2, 2, [[0.,.500000000000000000],[-.500000000000000000,0.]])`
- expected: `Matrix(2, 2, [[0.,.500000000000000000],[-.500000000000000000,0.]])`
- residual_or_error: `0.`
- tolerance: `0.`

## G004 - Trace normalization for T1

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: exact
- actual: `.500000000000000000`
- expected: `.500000000000000000`
- residual_or_error: `0.`
- tolerance: `0.`

## G005 - Trace normalization for T2

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: exact
- actual: `.500000000000000000`
- expected: `.500000000000000000`
- residual_or_error: `0.`
- tolerance: `0.`

## G006 - Trace normalization for T3

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: exact
- actual: `.500000000000000000`
- expected: `.500000000000000000`
- residual_or_error: `0.`
- tolerance: `0.`

## G007 - Off-diagonal trace normalization

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## G008 - Fundamental Casimir is 3/4 I

- paper_location: sec:pr2_nonabelian_generator_algebra
- kind: matrix
- actual: `Matrix(2, 2, [[.750000000000000000,0.],[0.,.750000000000000000]])`
- expected: `Matrix(2, 2, [[.750000000000000000,0.],[0.,.750000000000000000]])`
- residual_or_error: `0.`
- tolerance: `0.`

## G009 - j=0 spectral value numerator

- paper_location: sec:pr2_compact_weak_isospin_operator
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## G010 - j=1/2 spectral value numerator

- paper_location: sec:pr2_compact_weak_isospin_operator
- kind: exact
- actual: `.750000000000000000`
- expected: `.750000000000000000`
- residual_or_error: `0.`
- tolerance: `0.`

## G011 - j=1 adjoint Casimir

- paper_location: sec:pr2_compact_weak_isospin_operator
- kind: exact
- actual: `2.`
- expected: `2.`
- residual_or_error: `0.`
- tolerance: `0.`

## G012 - T+ raises down to up

- paper_location: sec:pr2_charged_current_topological_ladder
- kind: vector
- actual: `Vector(2, [1.,0.])`
- expected: `Vector(2, [1.,0.])`
- residual_or_error: `0.`
- tolerance: `0.`

## G013 - T- lowers up to down

- paper_location: sec:pr2_charged_current_topological_ladder
- kind: vector
- actual: `Vector(2, [0.,1.])`
- expected: `Vector(2, [0.,1.])`
- residual_or_error: `0.`
- tolerance: `0.`

## G014 - T+ annihilates up

- paper_location: sec:pr2_charged_current_topological_ladder
- kind: vector
- actual: `Vector(2, [0.,0.])`
- expected: `Vector(2, [0.,0.])`
- residual_or_error: `0.`
- tolerance: `0.`

## G015 - T- annihilates down

- paper_location: sec:pr2_charged_current_topological_ladder
- kind: vector
- actual: `Vector(2, [0.,0.])`
- expected: `Vector(2, [0.,0.])`
- residual_or_error: `0.`
- tolerance: `0.`

## G016 - Q annihilates the locking direction

- paper_location: sec:pr2_compact_electroweak_order_direction
- kind: vector
- actual: `Vector(2, [0.,0.])`
- expected: `Vector(2, [0.,0.])`
- residual_or_error: `0.`
- tolerance: `0.`

## G017 - [Q,T+]=T+

- paper_location: sec:pr2_charged_current_ladder
- kind: matrix
- actual: `Matrix(2, 2, [[0.,1.],[0.,0.]])`
- expected: `Matrix(2, 2, [[0.,1.],[0.,0.]])`
- residual_or_error: `0.`
- tolerance: `0.`

## G018 - [Q,T-]=-T-

- paper_location: sec:pr2_charged_current_ladder
- kind: matrix
- actual: `Matrix(2, 2, [[0.,0.],[-1.,0.]])`
- expected: `Matrix(2, 2, [[0.,0.],[-1.,0.]])`
- residual_or_error: `0.`
- tolerance: `0.`

## EW001 - Neutral mass matrix has zero determinant

- paper_location: sec:pr2_electroweak_connection_mass_ledger
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## EW002 - Nonzero neutral eigenvalue is MZ^2

- paper_location: sec:pr2_electroweak_connection_mass_ledger
- kind: exact
- actual: `.250000000000000000*(g0^2+gp0^2)*vv^2`
- expected: `.250000000000000000*(g0^2+gp0^2)*vv^2`
- residual_or_error: `0.`
- tolerance: `0.`

## EW003 - rho_EW tree-level identity

- paper_location: sec:pr2_tree_level_electroweak_consistency
- kind: exact
- actual: `1.`
- expected: `1.`
- residual_or_error: `0.`
- tolerance: `0.`

## EW004 - Charged Fermi contact coefficient

- paper_location: sec:pr2_charged_weak_projection_fermi_limit
- kind: exact
- actual: `.500000000000000000/vv^2`
- expected: `.500000000000000000/vv^2`
- residual_or_error: `0.`
- tolerance: `0.`

## EW005 - Neutral-current contact coefficient

- paper_location: sec:pr2_neutral_current_projection
- kind: exact
- actual: `.500000000000000000/vv^2`
- expected: `.500000000000000000/vv^2`
- residual_or_error: `0.`
- tolerance: `0.`

## EW006 - Broken compact directions

- paper_location: sec:pr2_compact_order_field_counting
- kind: exact
- actual: `3.`
- expected: `3.`
- residual_or_error: `0.`
- tolerance: `0.`

## EW007 - One scalar order-mode remains

- paper_location: sec:pr2_compact_order_field_counting
- kind: exact
- actual: `1.`
- expected: `1.`
- residual_or_error: `0.`
- tolerance: `0.`

## EW008 - hWW coupling ratio

- paper_location: sec:pr2_order_mode_gauge_boson_couplings
- kind: exact
- actual: `.500000000000000000*vv*g0^2`
- expected: `.500000000000000000*vv*g0^2`
- residual_or_error: `0.`
- tolerance: `0.`

## EW009 - hZZ coupling ratio

- paper_location: sec:pr2_order_mode_gauge_boson_couplings
- kind: exact
- actual: `.500000000000000000*(g0^2+gp0^2)*vv`
- expected: `.500000000000000000*(g0^2+gp0^2)*vv`
- residual_or_error: `0.`
- tolerance: `0.`

## B001 - Radial stiffness gap

- paper_location: sec:pr2_boundary_ledger_electroweak_lift
- kind: numeric
- actual: `3.052966743096`
- expected: `3.052966743096`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## B002 - Compact boundary stiffness

- paper_location: sec:pr2_boundary_ledger_electroweak_lift
- kind: numeric
- actual: `10.905007182855176`
- expected: `10.905007182855176`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## B003 - Compact boundary cofactor

- paper_location: sec:pr2_boundary_ledger_electroweak_lift
- kind: numeric
- actual: `.796684464847899053`
- expected: `.796684464847899`
- residual_or_error: `.532012574701195219e-16`
- tolerance: `.100000000000000000e-11`

## B004 - PR boundary alpha inverse

- paper_location: sec:pr2_boundary_ledger_electroweak_lift
- kind: numeric
- actual: `137.036361812007`
- expected: `137.036361812007`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## B005 - Generation suppression ratio

- paper_location: sec:pr2_boundary_ledger_electroweak_lift
- kind: numeric
- actual: `.730567574591279776e-1`
- expected: `.73056757459128e-1`
- residual_or_error: `.223633879086136530e-16`
- tolerance: `.100000000000000000e-11`

## B006 - Normalized weak boundary deficit

- paper_location: sec:pr2_weak_mixing_boundary_closure
- kind: numeric
- actual: `.186442367018109904e-1`
- expected: `.18644236701811e-1`
- residual_or_error: `.957115989414031508e-17`
- tolerance: `.100000000000000000e-11`

## B007 - Weak mixing sin^2

- paper_location: sec:pr2_weak_mixing_boundary_closure
- kind: numeric
- actual: `.231355763298189010`
- expected: `.231355763298189`
- residual_or_error: `.957115989414031508e-17`
- tolerance: `.100000000000000000e-11`

## B008 - Weak mixing cos^2

- paper_location: sec:pr2_weak_mixing_boundary_closure
- kind: numeric
- actual: `.768644236701810990`
- expected: `.768644236701811`
- residual_or_error: `.957115989414031508e-17`
- tolerance: `.100000000000000000e-11`

## B009 - g'/g = tan theta_W

- paper_location: sec:pr2_weak_mixing_boundary_closure
- kind: numeric
- actual: `.548627374785032013`
- expected: `.548627374785032`
- residual_or_error: `.125350727742257228e-16`
- tolerance: `.100000000000000000e-11`

## B010 - Dimensionless weak-order factor

- paper_location: sec:pr2_dimensionless_weak_order_factor
- kind: numeric
- actual: `2.00998412459095204`
- expected: `2.0099841245909515`
- residual_or_error: `.535639547848667645e-15`
- tolerance: `.100000000000000000e-11`

## B011 - sqrt Xi

- paper_location: sec:pr2_dimensionless_weak_order_factor
- kind: numeric
- actual: `1.41773908903964133`
- expected: `1.417739089039641`
- residual_or_error: `.325935810610193910e-15`
- tolerance: `.100000000000000000e-11`

## B012 - Terminal weak overlap

- paper_location: sec:pr2_terminal_weak_displacement_overlap
- kind: numeric
- actual: `.997513275401798772`
- expected: `.997513275401799`
- residual_or_error: `.228035557107662303e-15`
- tolerance: `.100000000000000000e-11`

## B013 - Base hierarchy action

- paper_location: sec:pr2_compact_spectral_hierarchy_action
- kind: numeric
- actual: `37.1800400711638244`
- expected: `37.18004007116382`
- residual_or_error: `.442676273120462877e-14`
- tolerance: `.100000000000000000e-11`

## B014 - Second-order action correction

- paper_location: sec:pr2_compact_spectral_hierarchy_action
- kind: numeric
- actual: `-.589204098090983842e-3`
- expected: `-.589204098090984800e-3`
- residual_or_error: `.957654500464347892e-18`
- tolerance: `.100000000000000000e-11`

## B015 - Total hierarchy action

- paper_location: sec:pr2_compact_spectral_hierarchy_action
- kind: numeric
- actual: `37.1794508670657334`
- expected: `37.17945086706573`
- residual_or_error: `.344292038570509312e-14`
- tolerance: `.100000000000000000e-11`

## B016 - Weak displacement anchor

- paper_location: sec:pr2_compact_spectral_hierarchy_action
- kind: numeric
- actual: `173.670598344728099`
- expected: `173.67059834472832`
- residual_or_error: `.220678682230039062e-12`
- tolerance: `.100000000000000000e-9`

## B017 - Generated electroweak vacuum scale

- paper_location: sec:pr2_generated_weak_scale_fermi_constant
- kind: numeric
- actual: `246.219595890224256`
- expected: `246.21959589022453`
- residual_or_error: `.273721042809304518e-12`
- tolerance: `.100000000000000000e-9`

## B018 - Generated Fermi constant

- paper_location: sec:pr2_generated_weak_scale_fermi_constant
- kind: numeric
- actual: `.116637922017599753e-4`
- expected: `.116637922017599500e-4`
- residual_or_error: `.252991573842367379e-19`
- tolerance: `.100000000000000000e-15`

## B019 - Weak-scale diagnostic residual

- paper_location: sec:pr2_generated_weak_scale_fermi_constant
- kind: numeric
- actual: `-.222987535587181206e-6`
- expected: `-.223000000000000000e-6`
- residual_or_error: `.124644128187938465e-10`
- tolerance: `.100000000000000000e-8`

## B020 - Fermi diagnostic residual

- paper_location: sec:pr2_generated_weak_scale_fermi_constant
- kind: numeric
- actual: `.445975220344729845e-6`
- expected: `.446000000000000000e-6`
- residual_or_error: `.247796552701551171e-10`
- tolerance: `.100000000000000000e-8`

## B021 - Diagnostic W mass using alpha(MZ)^-1

- paper_location: sec:pr2_mass_geometry_diagnostic_coupling
- kind: numeric
- actual: `80.2100447472722609`
- expected: `80.210045`
- residual_or_error: `.252727739089444438e-6`
- tolerance: `.100000000000000000e-5`

## B022 - Diagnostic Z mass using alpha(MZ)^-1

- paper_location: sec:pr2_mass_geometry_diagnostic_coupling
- kind: numeric
- actual: `91.4884081211357968`
- expected: `91.488408`
- residual_or_error: `.121135796789747514e-6`
- tolerance: `.100000000000000000e-5`

## A001 - u_L charge

- paper_location: sec:pr2_residual_em_charges_fermion_ledger
- kind: exact
- actual: `.666666666666666667`
- expected: `.666666666666666667`
- residual_or_error: `0.`
- tolerance: `0.`

## A002 - d_L charge

- paper_location: sec:pr2_residual_em_charges_fermion_ledger
- kind: exact
- actual: `-.333333333333333333`
- expected: `-.333333333333333333`
- residual_or_error: `0.`
- tolerance: `0.`

## A003 - nu_L charge

- paper_location: sec:pr2_residual_em_charges_fermion_ledger
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A004 - e_L charge

- paper_location: sec:pr2_residual_em_charges_fermion_ledger
- kind: exact
- actual: `-1.`
- expected: `-1.`
- residual_or_error: `0.`
- tolerance: `0.`

## A005 - Pure color anomaly

- paper_location: sec:pr2_pure_color_anomaly
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A006 - Mixed color-hypercharge anomaly

- paper_location: sec:pr2_mixed_color_hypercharge_anomaly
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A007 - Mixed weak-hypercharge anomaly

- paper_location: sec:pr2_mixed_weak_hypercharge_anomaly
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A008 - Mixed gravitational-hypercharge anomaly

- paper_location: sec:pr2_mixed_gravitational_hypercharge_anomaly
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A009 - Cubic hypercharge anomaly

- paper_location: sec:pr2_cubic_hypercharge_anomaly
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## A010 - One-generation Witten parity

- paper_location: sec:pr2_witten_global_anomaly
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## A011 - Three-generation Witten parity

- paper_location: sec:pr2_three_sheet_representation_ledger
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## F001 - Generation count from compact quotient

- paper_location: sec:pr2_generation_origin_flavor_sheets
- kind: exact
- actual: `3.`
- expected: `3.`
- residual_or_error: `0.`
- tolerance: `0.`

## F002 - First sheet eta

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `.533728981044185140e-2`
- expected: `.5337289810442e-2`
- residual_or_error: `.148601002692423966e-15`
- tolerance: `.100000000000000000e-11`

## F003 - Second sheet eta

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `.730567574591279776e-1`
- expected: `.73056757459128e-1`
- residual_or_error: `.223633879086136530e-16`
- tolerance: `.100000000000000000e-11`

## F004 - Third sheet eta

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `1.`
- expected: `1.`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## F005 - Sheet hierarchy ordering

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## F006 - Successive hierarchy ratio

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `13.6879877341867484`
- expected: `13.6879877341867`
- residual_or_error: `.484439267670805688e-13`
- tolerance: `.100000000000000000e-9`

## F007 - First terminal matter overlap

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `.532401744058249688e-2`
- expected: `.5324017440582e-2`
- residual_or_error: `.496877531006077460e-15`
- tolerance: `.100000000000000000e-11`

## F008 - Second terminal matter overlap

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `.728750854232895430e-1`
- expected: `.72875085423290e-1`
- residual_or_error: `.456952794538201804e-15`
- tolerance: `.100000000000000000e-11`

## F009 - Third terminal matter overlap

- paper_location: sec:pr2_generation_sheet_overlap_hierarchy_main
- kind: numeric
- actual: `.997513275401798772`
- expected: `.997513275401799`
- residual_or_error: `.228035557107662303e-15`
- tolerance: `.100000000000000000e-11`

## F010 - Charged-lepton sector factor

- paper_location: sec:pr2_sector_specific_compact_charge_norms
- kind: numeric
- actual: `1.14611351491825596`
- expected: `1.146113514918256`
- residual_or_error: `.447267758172273060e-16`
- tolerance: `.100000000000000000e-11`

## F011 - Up-quark sector factor

- paper_location: sec:pr2_sector_specific_compact_charge_norms
- kind: numeric
- actual: `1.18670060239554928`
- expected: `1.186700602395549`
- residual_or_error: `.276182453122431776e-15`
- tolerance: `.100000000000000000e-11`

## F012 - Down-quark sector factor

- paper_location: sec:pr2_sector_specific_compact_charge_norms
- kind: numeric
- actual: `1.16234834990917328`
- expected: `1.162348349909173`
- residual_or_error: `.283636915758636327e-15`
- tolerance: `.100000000000000000e-11`

## F013 - Dirac-neutrino sector factor

- paper_location: sec:pr2_sector_specific_compact_charge_norms
- kind: numeric
- actual: `1.07305675745912798`
- expected: `1.073056757459128`
- residual_or_error: `.223633879086136530e-16`
- tolerance: `.100000000000000000e-11`

## F014 - D_l first entry

- paper_location: sec:pr2_sector_specific_overlap_spectra
- kind: numeric
- actual: `.610192834231210242e-2`
- expected: `.6101928e-2`
- residual_or_error: `.342312102423994476e-9`
- tolerance: `.100000000000000000e-8`

## F015 - D_l second entry

- paper_location: sec:pr2_sector_specific_overlap_spectra
- kind: numeric
- actual: `.835231203044545368e-1`
- expected: `.83523120e-1`
- residual_or_error: `.304454536802267474e-9`
- tolerance: `.100000000000000000e-8`

## F016 - D_l third entry

- paper_location: sec:pr2_sector_specific_overlap_spectra
- kind: numeric
- actual: `1.14326344624837786`
- expected: `1.143263446`
- residual_or_error: `.248377858058853816e-9`
- tolerance: `.100000000000000000e-8`

## F017 - Up/down sheetwise sector ratio

- paper_location: sec:pr2_sector_specific_overlap_spectra
- kind: numeric
- actual: `1.02095090726310997`
- expected: `1.02095090726311`
- residual_or_error: `.255615512036559056e-16`
- tolerance: `.100000000000000000e-11`

## F018 - Charged-lepton hypercharge neutrality

- paper_location: sec:pr2_hypercharge_neutral_order_terms
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## F019 - Down-quark hypercharge neutrality

- paper_location: sec:pr2_hypercharge_neutral_order_terms
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## F020 - Up-quark hypercharge neutrality

- paper_location: sec:pr2_hypercharge_neutral_order_terms
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## F021 - Dirac-neutrino hypercharge neutrality

- paper_location: sec:pr2_hypercharge_neutral_order_terms
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## L001 - Koide sheet phase

- paper_location: sec:pr2_three_sheet_square_root_flavor_geometry
- kind: numeric
- actual: `.222222222222222222`
- expected: `.222222222222222222`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## L002 - Three-sheet cosine sum

- paper_location: sec:pr2_koide_identity_three_sheet_geometry
- kind: numeric
- actual: `-.11e-58`
- expected: `0.`
- residual_or_error: `.11e-58`
- tolerance: `.100000000000000000e-11`

## L003 - Three-sheet cosine-square sum

- paper_location: sec:pr2_koide_identity_three_sheet_geometry
- kind: numeric
- actual: `1.50000000000000000`
- expected: `1.50000000000000000`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## L004 - Charged-lepton C1

- paper_location: sec:pr2_charged_lepton_compact_scale
- kind: numeric
- actual: `.996286606565180038`
- expected: `.996286606565180`
- residual_or_error: `.381534411790102380e-16`
- tolerance: `.100000000000000000e-11`

## L005 - Charged-lepton C2

- paper_location: sec:pr2_charged_lepton_compact_scale
- kind: numeric
- actual: `.998776379293596691`
- expected: `.998776379293597`
- residual_or_error: `.309058127499445852e-15`
- tolerance: `.100000000000000000e-11`

## L006 - Charged-lepton compact scale in MeV

- paper_location: sec:pr2_charged_lepton_compact_scale
- kind: numeric
- actual: `313.850332182569523`
- expected: `313.850332183`
- residual_or_error: `.430477315493039586e-9`
- tolerance: `.100000000000000000e-8`

## L007 - Electron mass candidate

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `.510984462863176445`
- expected: `.510984463`
- residual_or_error: `.136823554945338334e-9`
- tolerance: `.100000000000000000e-8`

## L008 - Muon mass candidate

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `105.656418843374400`
- expected: `105.656418843`
- residual_or_error: `.374399595942642078e-9`
- tolerance: `.100000000000000000e-8`

## L009 - Tau mass candidate

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `1776.93458978917956`
- expected: `1776.934589789`
- residual_or_error: `.179560066044458740e-9`
- tolerance: `.100000000000000000e-8`

## L010 - Koide ratio

- paper_location: sec:pr2_koide_identity_three_sheet_geometry
- kind: numeric
- actual: `.666666666666666667`
- expected: `.666666666666666667`
- residual_or_error: `.2e-59`
- tolerance: `.100000000000000000e-11`

## L011 - Electron ppm residual

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `-28.3506195532396795`
- expected: `-28.35`
- residual_or_error: `.619553239679530328e-3`
- tolerance: `.100000000000000000e-1`

## L012 - Muon ppm residual

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `-18.5187082078543225`
- expected: `-18.52`
- residual_or_error: `.129179214567748718e-2`
- tolerance: `.100000000000000000e-1`

## L013 - Tau ppm residual

- paper_location: sec:pr2_generated_charged_lepton_masses
- kind: numeric
- actual: `2.58298817598896189`
- expected: `2.58`
- residual_or_error: `.298817598896188621e-2`
- tolerance: `.100000000000000000e-1`

## Q001 - Compact strong-coupling candidate

- paper_location: sec:pr2_compact_boundary_strong_coupling_candidate
- kind: numeric
- actual: `.117861507469149537`
- expected: `.117861507469150`
- residual_or_error: `.462961090822099743e-15`
- tolerance: `.100000000000000000e-11`

## Q002 - Top threshold candidate

- paper_location: sec:pr2_pr_derived_heavy_quark_thresholds
- kind: numeric
- actual: `172.813973266662166`
- expected: `172.8139732666624`
- residual_or_error: `.233527622250817874e-12`
- tolerance: `.100000000000000000e-9`

## Q003 - Bottom threshold candidate

- paper_location: sec:pr2_pr_derived_heavy_quark_thresholds
- kind: numeric
- actual: `4.16645048267534714`
- expected: `4.1664504826753515`
- residual_or_error: `.436022934994666551e-14`
- tolerance: `.100000000000000000e-11`

## Q004 - Charm threshold candidate

- paper_location: sec:pr2_pr_derived_heavy_quark_thresholds
- kind: numeric
- actual: `1.27496481425746374`
- expected: `1.274964814257465`
- residual_or_error: `.125785264977980765e-14`
- tolerance: `.100000000000000000e-11`

## Q005 - Heavy-threshold ordering

- paper_location: sec:pr2_pr_derived_heavy_quark_thresholds
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## Q006 - beta0 for nf=3

- paper_location: sec:pr2_qcd_running_ledger_main
- kind: exact
- actual: `9.`
- expected: `9.`
- residual_or_error: `0.`
- tolerance: `0.`

## Q007 - beta0 for nf=4

- paper_location: sec:pr2_qcd_running_ledger_main
- kind: exact
- actual: `8.33333333333333333`
- expected: `8.33333333333333333`
- residual_or_error: `0.`
- tolerance: `0.`

## Q008 - beta0 for nf=5

- paper_location: sec:pr2_qcd_running_ledger_main
- kind: exact
- actual: `7.66666666666666667`
- expected: `7.66666666666666667`
- residual_or_error: `0.`
- tolerance: `0.`

## Q009 - beta0 for nf=6

- paper_location: sec:pr2_qcd_running_ledger_main
- kind: exact
- actual: `7.`
- expected: `7.`
- residual_or_error: `0.`
- tolerance: `0.`

## Q010 - Mass-running exponent for nf=5

- paper_location: sec:pr2_qcd_running_ledger_main
- kind: exact
- actual: `.521739130434782609`
- expected: `.521739130434782609`
- residual_or_error: `0.`
- tolerance: `0.`

## Q011 - Lambda_6 from three-loop matching

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.877675850742605169e-1`
- expected: `.8776758507426047e-1`
- residual_or_error: `.468837399981731434e-16`
- tolerance: `.100000000000000000e-11`

## Q012 - Lambda_5 from alpha_3 at MZ

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.207433087300412155`
- expected: `.2074330873004123`
- residual_or_error: `.145011103774197560e-15`
- tolerance: `.100000000000000000e-11`

## Q013 - Lambda_4 from bottom matching

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.286111791803031097`
- expected: `.2861117918030313`
- residual_or_error: `.203467028383831242e-15`
- tolerance: `.100000000000000000e-11`

## Q014 - Lambda_3 from charm matching

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.324652496410777907`
- expected: `.3246524964107782`
- residual_or_error: `.292752107282529297e-15`
- tolerance: `.100000000000000000e-11`

## Q015 - Top-threshold coupling continuity

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `-.1e-59`
- expected: `0.`
- residual_or_error: `.1e-59`
- tolerance: `.100000000000000000e-11`

## Q016 - Bottom-threshold coupling continuity

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `-.1e-59`
- expected: `0.`
- residual_or_error: `.1e-59`
- tolerance: `.100000000000000000e-11`

## Q017 - Charm-threshold coupling continuity

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `-.2e-59`
- expected: `0.`
- residual_or_error: `.2e-59`
- tolerance: `.100000000000000000e-11`

## Q018 - b running diagnostic at MZ

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `2.98078465819592825`
- expected: `2.9807846581959314`
- residual_or_error: `.315481661117851625e-14`
- tolerance: `.100000000000000000e-11`

## Q019 - c running diagnostic at bottom threshold

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.989217286169865756`
- expected: `.9892172861698667`
- residual_or_error: `.944475417473657970e-15`
- tolerance: `.100000000000000000e-11`

## Q020 - c running diagnostic at MZ

- paper_location: sec:pr2_qcd_threshold_ledger
- kind: numeric
- actual: `.707711209457114170`
- expected: `.7077112094571149`
- residual_or_error: `.730010663542351304e-15`
- tolerance: `.100000000000000000e-11`

## Q021 - Compact confinement average

- paper_location: sec:pr2_light_sector_confinement_average_main
- kind: numeric
- actual: `.898342232423949527`
- expected: `.8983422324239495`
- residual_or_error: `.266006287350597610e-16`
- tolerance: `.100000000000000000e-11`

## Q022 - Confinement endpoint reconstructs c_bc

- paper_location: sec:pr2_light_sector_confinement_average_main
- kind: numeric
- actual: `.796684464847899053`
- expected: `.796684464847899053`
- residual_or_error: `.1e-59`
- tolerance: `.100000000000000000e-11`

## Q023 - Strange-quark low-energy candidate

- paper_location: sec:pr2_light_quark_hierarchy_candidate
- kind: numeric
- actual: `94.0285105375763436`
- expected: `94.028510538`
- residual_or_error: `.423656386315312133e-9`
- tolerance: `.100000000000000000e-8`

## Q024 - Down-quark low-energy candidate

- paper_location: sec:pr2_light_quark_hierarchy_candidate
- kind: numeric
- actual: `4.76103949316045680`
- expected: `4.761039493`
- residual_or_error: `.160456801372978267e-9`
- tolerance: `.100000000000000000e-8`

## Q025 - Up-quark low-energy candidate

- paper_location: sec:pr2_light_quark_hierarchy_candidate
- kind: numeric
- actual: `2.14646259488632039`
- expected: `2.146462595`
- residual_or_error: `.113679610420793251e-9`
- tolerance: `.100000000000000000e-8`

## Q026 - Six-quark hierarchy ordering

- paper_location: sec:pr2_six_quark_hierarchy_candidate
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## M001 - Compact Cabibbo sheet angle

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.225019996525934957`
- expected: `.225019996525935`
- residual_or_error: `.431842500230327661e-16`
- tolerance: `.100000000000000000e-11`

## M002 - Compact CKM hierarchy coefficient

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.822683296413403325`
- expected: `.822683296413403`
- residual_or_error: `.324731650113514040e-15`
- tolerance: `.100000000000000000e-11`

## M003 - Compact unitarity-apex radius

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.398035078485257788`
- expected: `.398035078485258`
- residual_or_error: `.212422665345077545e-15`
- tolerance: `.100000000000000000e-11`

## M004 - CKM phase in radians

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `1.18374145146977359`
- expected: `1.1837414514697735`
- residual_or_error: `.905317921628736293e-16`
- tolerance: `.100000000000000000e-11`

## M005 - CKM s23

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.416557450734303935e-1`
- expected: `.41655745073430e-1`
- residual_or_error: `.393471000359130059e-15`
- tolerance: `.100000000000000000e-11`

## M006 - CKM s13

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.373093229727820968e-2`
- expected: `.3730932297278e-2`
- residual_or_error: `.209677526981548855e-15`
- tolerance: `.100000000000000000e-11`

## M007 - CKM absolute matrix

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: matrix
- actual: `Matrix(3, 3, [[.974347364201096444,.225018430397532215,.373093229727820968e-2],[.224881886831690032,.973495228561057413,.416554551514389969e-1],[.868048670264986654e-2,.409114403350155611e-1,.999125068847899332]])`
- expected: `Matrix(3, 3, [[.974347364,.225018430,.3730932e-2],[.224881887,.973495229,.41655455e-1],[.8680487e-2,.40911440e-1,.999125069]])`
- residual_or_error: `.438942587495627937e-9`
- tolerance: `.100000000000000000e-8`

## M008 - CKM unitarity

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: matrix
- actual: `Matrix(3, 3, [[1.00000000000000000+0.*I,-.929e-60+0.*I,-.1e-61+.1e-61*I],[-.929e-60+0.*I,1.00000000000000000+0.*I,0.+0.*I],[-.1e-61-.1e-61*I,0.+0.*I,1.00000000000000000+0.*I]])`
- expected: `Matrix(3, 3, [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])`
- residual_or_error: `.929e-60`
- tolerance: `.100000000000000000e-13`

## M009 - CKM Jarlskog invariant

- paper_location: sec:pr2_ckm_compact_mixing_candidate
- kind: numeric
- actual: `.315260567707480051e-4`
- expected: `.315260567700000000e-4`
- residual_or_error: `.748005135375042023e-15`
- tolerance: `.100000000000000000e-12`

## M010 - PMNS solar sin^2

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `.299447410807983176`
- expected: `.299447410807983`
- residual_or_error: `.175533542911686587e-15`
- tolerance: `.100000000000000000e-11`

## M011 - PMNS solar angle

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `33.1763566434167334`
- expected: `33.176356643`
- residual_or_error: `.416733431439128417e-9`
- tolerance: `.100000000000000000e-8`

## M012 - PMNS atmospheric sin^2

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `.565008899090616193`
- expected: `.565008899090616`
- residual_or_error: `.193267295401726428e-15`
- tolerance: `.100000000000000000e-11`

## M013 - PMNS atmospheric angle

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `48.7353104030270103`
- expected: `48.735310403`
- residual_or_error: `.270102818329667741e-10`
- tolerance: `.100000000000000000e-8`

## M014 - PMNS reactor sin^2

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `.222702701247427246e-1`
- expected: `.22270270124743e-1`
- residual_or_error: `.275412877195201028e-15`
- tolerance: `.100000000000000000e-11`

## M015 - PMNS reactor angle

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `8.58243805858002142`
- expected: `8.582438059`
- residual_or_error: `.419978577826753247e-9`
- tolerance: `.100000000000000000e-8`

## M016 - PMNS CP phase

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `3.41468045413614493`
- expected: `3.414680454`
- residual_or_error: `.136144927217798787e-9`
- tolerance: `.100000000000000000e-8`

## M017 - PMNS absolute matrix

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: matrix
- actual: `Matrix(3, 3, [[.827617722015498342,.541090229149570383,.149232269046418793],[.271685029609593918,.611360160953467273,.743253656758568976],[.491157969386542060,.577460057075652640,.652153150410448151]])`
- expected: `Matrix(3, 3, [[.827618,.541090,.149232],[.271685,.611360,.743254],[.491158,.577460,.652153]])`
- residual_or_error: `.343241431023574474e-6`
- tolerance: `.100000000000000000e-5`

## M018 - PMNS unitarity

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: matrix
- actual: `Matrix(3, 3, [[1.00000000000000000+0.*I,0.+.1e-60*I,.1e-59+0.*I],[0.-.1e-60*I,1.00000000000000000+0.*I,.1e-59+.1e-61*I],[.1e-59+0.*I,.1e-59-.1e-61*I,1.00000000000000000+0.*I]])`
- expected: `Matrix(3, 3, [[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])`
- residual_or_error: `.100004999875006250e-59`
- tolerance: `.100000000000000000e-13`

## M019 - PMNS Jarlskog invariant

- paper_location: sec:pr2_pmns_compact_lepton_mixing_candidate
- kind: numeric
- actual: `-.893554000041493053e-2`
- expected: `-.893554000000000000e-2`
- residual_or_error: `.414930533544771142e-12`
- tolerance: `.100000000000000000e-8`

## N001 - Compact neutrino loss factor

- paper_location: sec:pr2_neutrino_normal_ordering_singlet_channel
- kind: numeric
- actual: `.985146426260720153`
- expected: `.985147`
- residual_or_error: `.573739279847386235e-6`
- tolerance: `.100000000000000000e-5`

## N002 - Solar-to-atmospheric splitting ratio

- paper_location: sec:pr2_neutrino_normal_ordering_singlet_channel
- kind: numeric
- actual: `.296455166776998529e-1`
- expected: `.296455166800000000e-1`
- residual_or_error: `.230014712944296026e-11`
- tolerance: `.100000000000000000e-10`

## N003 - Massless residual compact-singlet sheet

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `.100000000000000000e-11`

## N004 - Second neutrino mass

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.862728301014426747e-2`
- expected: `.862728301000000000e-2`
- residual_or_error: `.144267472276639146e-12`
- tolerance: `.100000000000000000e-11`

## N005 - Third neutrino mass

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.501065536689642452e-1`
- expected: `.501065536700000000e-1`
- residual_or_error: `.103575480169002268e-11`
- tolerance: `.200000000000000000e-11`

## N006 - Normal-ordering hierarchy

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## N007 - Solar mass-squared splitting

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.744300121371239327e-4`
- expected: `.744300121400000000e-4`
- residual_or_error: `.287606727504339705e-14`
- tolerance: `.100000000000000000e-12`

## N008 - Atmospheric mass-squared splitting

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.251066672058079426e-2`
- expected: `.251066672100000000e-2`
- residual_or_error: `.419205738218609868e-12`
- tolerance: `.100000000000000000e-11`

## N009 - Splitting ratio

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.296455166776998529e-1`
- expected: `.296455166800000000e-1`
- residual_or_error: `.230014712944296026e-11`
- tolerance: `.100000000000000000e-10`

## N010 - Cosmological neutrino mass sum

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.587338366791085127e-1`
- expected: `.587338366800000000e-1`
- residual_or_error: `.891487329413383529e-12`
- tolerance: `.100000000000000000e-11`

## N011 - Beta-decay effective mass

- paper_location: sec:pr2_generated_neutrino_spectrum
- kind: numeric
- actual: `.881502940990815359e-2`
- expected: `.881502941000000000e-2`
- residual_or_error: `.918464094557351682e-13`
- tolerance: `.100000000000000000e-11`

## N012 - Equivalent Dirac Yukawa diagnostic

- paper_location: sec:pr2_majorana_dominant_compact_singlet_projection
- kind: numeric
- actual: `.287797433450495055e-12`
- expected: `.288000000000000000e-12`
- residual_or_error: `.202566549504945021e-15`
- tolerance: `.100000000000000000e-14`

## N013 - Majorana interference phase

- paper_location: sec:pr2_majorana_phase_boundary
- kind: numeric
- actual: `2.82222535779253439`
- expected: `2.822225357793`
- residual_or_error: `.465611479554830962e-12`
- tolerance: `.100000000000000000e-11`

## N014 - Locked alpha31 phase

- paper_location: sec:pr2_majorana_phase_boundary
- kind: numeric
- actual: `3.36840095888523777`
- expected: `3.368400958885`
- residual_or_error: `.237766030755976160e-12`
- tolerance: `.100000000000000000e-11`

## N015 - Neutrinoless double-beta effective mass

- paper_location: sec:pr2_majorana_phase_boundary
- kind: numeric
- actual: `.150769447683466932e-2`
- expected: `.150769447700000000e-2`
- residual_or_error: `.165330676573813716e-12`
- tolerance: `.100000000000000000e-11`

## N016 - Flavor-basis Majorana matrix is symmetric

- paper_location: sec:pr2_flavor_basis_majorana_mass_matrix
- kind: matrix
- actual: `Matrix(3, 3, [[.172709882400942661e-2-.779194870638467771e-3*I,.773047608691543039e-2+.258670863784098678e-2*I,.158495035748896445e-2+.226965608849992365e-2*I],[.773047608691543039e-2+.258670863784098678e-2*I,-.237514333315425043e-1-.639897836019768861e-2*I,-.267111221999790915e-1-.545561572483763769e-2*I],[.158495035748896445e-2+.226965608849992365e-2*I,-.267111221999790915e-1-.545561572483763769e-2*I,-.178915085212936948e-1-.464737452267581652e-2*I]])`
- expected: `Matrix(3, 3, [[.172709882400942661e-2-.779194870638467771e-3*I,.773047608691543039e-2+.258670863784098678e-2*I,.158495035748896445e-2+.226965608849992365e-2*I],[.773047608691543039e-2+.258670863784098678e-2*I,-.237514333315425043e-1-.639897836019768861e-2*I,-.267111221999790915e-1-.545561572483763769e-2*I],[.158495035748896445e-2+.226965608849992365e-2*I,-.267111221999790915e-1-.545561572483763769e-2*I,-.178915085212936948e-1-.464737452267581652e-2*I]])`
- residual_or_error: `.2e-61`
- tolerance: `.100000000000000000e-13`

## SRC001 - Weak mixing section label present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `44176.`
- expected: `\label{sec:pr2_weak_mixing_boundary_closure}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC002 - Weak mixing numeric target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `45118.`
- expected: `0.231355763298189`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC003 - Generated weak scale target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `62059.`
- expected: `246.21959589022453`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC004 - Fermi constant target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `62241.`
- expected: `1.166379220175995`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC005 - Anomaly section label present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `98408.`
- expected: `\label{sec:pr2_fermion_representation_anomaly_cancellation}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC006 - Charged-lepton section label present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `132604.`
- expected: `\label{sec:pr2_charged_lepton_precision_candidate}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC007 - Electron candidate target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `141379.`
- expected: `0.510984463`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC008 - Strong-coupling target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `150891.`
- expected: `0.117861507469150`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC009 - QCD Lambda_6 target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `158231.`
- expected: `0.08776758507426047`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC010 - CKM Jarlskog target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `175986.`
- expected: `3.152605677`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC011 - PMNS Jarlskog target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `180891.`
- expected: `-8.935540`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC012 - m_beta_beta target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `198021.`
- expected: `1.507694477`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-DISPLAY-COUNT - Every top-level display block is inventoried

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `446.`
- expected: `446.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-LABEL-COUNT - LaTeX label count is stable

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `137.`
- expected: `137.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-LABEL-UNIQUE - All LaTeX labels are unique

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `137.`
- expected: `137.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-REFS-RESOLVED - Every ref/eqref target resolves to a label

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0001 - PR2-EQ-0001 lines 74-82 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0002 - PR2-EQ-0002 lines 86-94 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0003 - PR2-EQ-0003 lines 101-105 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0004 - PR2-EQ-0004 lines 107-115 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0005 - PR2-EQ-0005 lines 119-129 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0006 - PR2-EQ-0006 lines 131-141 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0007 - PR2-EQ-0007 lines 152-158 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0008 - PR2-EQ-0008 lines 160-166 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0009 - PR2-EQ-0009 lines 170-185 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0010 - PR2-EQ-0010 lines 194-196 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0011 - PR2-EQ-0011 lines 225-231 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0012 - PR2-EQ-0012 lines 234-240 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0013 - PR2-EQ-0013 lines 243-247 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0014 - PR2-EQ-0014 lines 250-252 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0015 - PR2-EQ-0015 lines 254-256 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0016 - PR2-EQ-0016 lines 259-267 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0017 - PR2-EQ-0017 lines 271-277 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0018 - PR2-EQ-0018 lines 279-287 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0019 - PR2-EQ-0019 lines 289-297 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0020 - PR2-EQ-0020 lines 340-350 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0021 - PR2-EQ-0021 lines 354-364 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0022 - PR2-EQ-0022 lines 366-368 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0023 - PR2-EQ-0023 lines 370-377 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0024 - PR2-EQ-0024 lines 379-386 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0025 - PR2-EQ-0025 lines 389-393 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0026 - PR2-EQ-0026 lines 395-401 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0027 - PR2-EQ-0027 lines 404-411 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0028 - PR2-EQ-0028 lines 413-419 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0029 - PR2-EQ-0029 lines 471-477 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0030 - PR2-EQ-0030 lines 479-485 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0031 - PR2-EQ-0031 lines 489-496 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0032 - PR2-EQ-0032 lines 498-505 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0033 - PR2-EQ-0033 lines 560-570 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0034 - PR2-EQ-0034 lines 578-584 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0035 - PR2-EQ-0035 lines 586-592 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0036 - PR2-EQ-0036 lines 594-598 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0037 - PR2-EQ-0037 lines 601-606 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0038 - PR2-EQ-0038 lines 609-613 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0039 - PR2-EQ-0039 lines 615-621 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0040 - PR2-EQ-0040 lines 627-631 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0041 - PR2-EQ-0041 lines 634-638 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0042 - PR2-EQ-0042 lines 640-646 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0043 - PR2-EQ-0043 lines 649-655 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0044 - PR2-EQ-0044 lines 657-667 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0045 - PR2-EQ-0045 lines 673-678 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0046 - PR2-EQ-0046 lines 680-685 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0047 - PR2-EQ-0047 lines 687-693 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0048 - PR2-EQ-0048 lines 695-703 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0049 - PR2-EQ-0049 lines 712-716 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0050 - PR2-EQ-0050 lines 718-732 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0051 - PR2-EQ-0051 lines 734-744 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0052 - PR2-EQ-0052 lines 751-753 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0053 - PR2-EQ-0053 lines 755-757 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0054 - PR2-EQ-0054 lines 759-766 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0055 - PR2-EQ-0055 lines 768-777 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0056 - PR2-EQ-0056 lines 779-787 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0057 - PR2-EQ-0057 lines 790-796 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0058 - PR2-EQ-0058 lines 802-813 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0059 - PR2-EQ-0059 lines 817-823 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0060 - PR2-EQ-0060 lines 831-833 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0061 - PR2-EQ-0061 lines 836-842 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0062 - PR2-EQ-0062 lines 844-850 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0063 - PR2-EQ-0063 lines 926-936 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0064 - PR2-EQ-0064 lines 938-950 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0065 - PR2-EQ-0065 lines 952-962 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0066 - PR2-EQ-0066 lines 965-971 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0067 - PR2-EQ-0067 lines 981-984 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0068 - PR2-EQ-0068 lines 987-996 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0069 - PR2-EQ-0069 lines 998-1002 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0070 - PR2-EQ-0070 lines 1004-1012 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0071 - PR2-EQ-0071 lines 1014-1020 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0072 - PR2-EQ-0072 lines 1023-1034 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0073 - PR2-EQ-0073 lines 1040-1052 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0074 - PR2-EQ-0074 lines 1054-1058 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0075 - PR2-EQ-0075 lines 1060-1070 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0076 - PR2-EQ-0076 lines 1079-1081 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0077 - PR2-EQ-0077 lines 1083-1089 status MANUSCRIPT mode paper-cleanup

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0078 - PR2-EQ-0078 lines 1091-1093 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0079 - PR2-EQ-0079 lines 1100-1102 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0080 - PR2-EQ-0080 lines 1105-1109 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0081 - PR2-EQ-0081 lines 1111-1117 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0082 - PR2-EQ-0082 lines 1120-1126 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0083 - PR2-EQ-0083 lines 1128-1136 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0084 - PR2-EQ-0084 lines 1138-1144 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0085 - PR2-EQ-0085 lines 1146-1152 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0086 - PR2-EQ-0086 lines 1154-1162 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0087 - PR2-EQ-0087 lines 1172-1183 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0088 - PR2-EQ-0088 lines 1185-1189 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0089 - PR2-EQ-0089 lines 1191-1202 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0090 - PR2-EQ-0090 lines 1204-1208 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0091 - PR2-EQ-0091 lines 1210-1214 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0092 - PR2-EQ-0092 lines 1217-1225 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0093 - PR2-EQ-0093 lines 1231-1242 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0094 - PR2-EQ-0094 lines 1244-1258 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0095 - PR2-EQ-0095 lines 1260-1276 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0096 - PR2-EQ-0096 lines 1282-1290 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0097 - PR2-EQ-0097 lines 1293-1295 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0098 - PR2-EQ-0098 lines 1297-1299 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0099 - PR2-EQ-0099 lines 1301-1307 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0100 - PR2-EQ-0100 lines 1313-1317 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0101 - PR2-EQ-0101 lines 1319-1324 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0102 - PR2-EQ-0102 lines 1385-1387 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0103 - PR2-EQ-0103 lines 1389-1393 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0104 - PR2-EQ-0104 lines 1395-1399 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0105 - PR2-EQ-0105 lines 1401-1409 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0106 - PR2-EQ-0106 lines 1417-1422 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0107 - PR2-EQ-0107 lines 1424-1432 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0108 - PR2-EQ-0108 lines 1434-1440 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0109 - PR2-EQ-0109 lines 1443-1449 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0110 - PR2-EQ-0110 lines 1451-1457 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0111 - PR2-EQ-0111 lines 1460-1467 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0112 - PR2-EQ-0112 lines 1474-1476 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0113 - PR2-EQ-0113 lines 1478-1488 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0114 - PR2-EQ-0114 lines 1490-1496 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0115 - PR2-EQ-0115 lines 1498-1506 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0116 - PR2-EQ-0116 lines 1510-1514 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0117 - PR2-EQ-0117 lines 1521-1531 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0118 - PR2-EQ-0118 lines 1533-1541 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0119 - PR2-EQ-0119 lines 1544-1563 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0120 - PR2-EQ-0120 lines 1569-1575 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0121 - PR2-EQ-0121 lines 1578-1586 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0122 - PR2-EQ-0122 lines 1588-1592 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0123 - PR2-EQ-0123 lines 1595-1603 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0124 - PR2-EQ-0124 lines 1605-1611 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0125 - PR2-EQ-0125 lines 1613-1619 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0126 - PR2-EQ-0126 lines 1622-1634 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0127 - PR2-EQ-0127 lines 1639-1644 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0128 - PR2-EQ-0128 lines 1646-1652 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0129 - PR2-EQ-0129 lines 1654-1667 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0130 - PR2-EQ-0130 lines 1670-1674 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0131 - PR2-EQ-0131 lines 1676-1688 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0132 - PR2-EQ-0132 lines 1690-1702 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0133 - PR2-EQ-0133 lines 1742-1748 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0134 - PR2-EQ-0134 lines 1750-1759 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0135 - PR2-EQ-0135 lines 1761-1773 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0136 - PR2-EQ-0136 lines 1777-1783 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0137 - PR2-EQ-0137 lines 1785-1791 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0138 - PR2-EQ-0138 lines 1798-1814 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0139 - PR2-EQ-0139 lines 1816-1828 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0140 - PR2-EQ-0140 lines 1830-1850 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0141 - PR2-EQ-0141 lines 1857-1859 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0142 - PR2-EQ-0142 lines 1861-1863 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0143 - PR2-EQ-0143 lines 1865-1877 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0144 - PR2-EQ-0144 lines 1884-1889 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0145 - PR2-EQ-0145 lines 1891-1896 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0146 - PR2-EQ-0146 lines 1898-1904 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0147 - PR2-EQ-0147 lines 1913-1923 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0148 - PR2-EQ-0148 lines 1925-1936 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0149 - PR2-EQ-0149 lines 1938-1945 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0150 - PR2-EQ-0150 lines 1947-1953 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0151 - PR2-EQ-0151 lines 1955-1968 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0152 - PR2-EQ-0152 lines 1972-1976 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0153 - PR2-EQ-0153 lines 1982-1986 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0154 - PR2-EQ-0154 lines 1988-1990 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0155 - PR2-EQ-0155 lines 1992-2000 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0156 - PR2-EQ-0156 lines 2002-2010 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0157 - PR2-EQ-0157 lines 2012-2021 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0158 - PR2-EQ-0158 lines 2023-2033 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0159 - PR2-EQ-0159 lines 2035-2045 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0160 - PR2-EQ-0160 lines 2048-2060 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0161 - PR2-EQ-0161 lines 2069-2076 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0162 - PR2-EQ-0162 lines 2079-2086 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0163 - PR2-EQ-0163 lines 2088-2094 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0164 - PR2-EQ-0164 lines 2096-2110 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0165 - PR2-EQ-0165 lines 2112-2122 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0166 - PR2-EQ-0166 lines 2130-2136 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0167 - PR2-EQ-0167 lines 2139-2151 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0168 - PR2-EQ-0168 lines 2161-2169 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0169 - PR2-EQ-0169 lines 2171-2175 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0170 - PR2-EQ-0170 lines 2184-2190 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0171 - PR2-EQ-0171 lines 2191-2201 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0172 - PR2-EQ-0172 lines 2202-2210 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0173 - PR2-EQ-0173 lines 2212-2220 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0174 - PR2-EQ-0174 lines 2222-2235 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0175 - PR2-EQ-0175 lines 2244-2252 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0176 - PR2-EQ-0176 lines 2256-2258 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0177 - PR2-EQ-0177 lines 2262-2270 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0178 - PR2-EQ-0178 lines 2274-2278 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0179 - PR2-EQ-0179 lines 2280-2287 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0180 - PR2-EQ-0180 lines 2290-2294 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0181 - PR2-EQ-0181 lines 2301-2311 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0182 - PR2-EQ-0182 lines 2318-2322 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0183 - PR2-EQ-0183 lines 2324-2338 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0184 - PR2-EQ-0184 lines 2340-2350 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0185 - PR2-EQ-0185 lines 2352-2358 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0186 - PR2-EQ-0186 lines 2360-2364 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0187 - PR2-EQ-0187 lines 2366-2370 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0188 - PR2-EQ-0188 lines 2372-2376 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0189 - PR2-EQ-0189 lines 2378-2384 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0190 - PR2-EQ-0190 lines 2386-2392 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0191 - PR2-EQ-0191 lines 2394-2400 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0192 - PR2-EQ-0192 lines 2403-2411 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0193 - PR2-EQ-0193 lines 2416-2424 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0194 - PR2-EQ-0194 lines 2426-2435 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0195 - PR2-EQ-0195 lines 2439-2446 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0196 - PR2-EQ-0196 lines 2448-2452 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0197 - PR2-EQ-0197 lines 2454-2458 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0198 - PR2-EQ-0198 lines 2460-2466 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0199 - PR2-EQ-0199 lines 2468-2474 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0200 - PR2-EQ-0200 lines 2476-2482 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0201 - PR2-EQ-0201 lines 2488-2500 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0202 - PR2-EQ-0202 lines 2503-2514 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0203 - PR2-EQ-0203 lines 2517-2525 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0204 - PR2-EQ-0204 lines 2527-2533 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0205 - PR2-EQ-0205 lines 2536-2551 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0206 - PR2-EQ-0206 lines 2553-2567 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0207 - PR2-EQ-0207 lines 2570-2576 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0208 - PR2-EQ-0208 lines 2578-2582 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0209 - PR2-EQ-0209 lines 2584-2592 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0210 - PR2-EQ-0210 lines 2598-2604 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0211 - PR2-EQ-0211 lines 2606-2616 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0212 - PR2-EQ-0212 lines 2657-2663 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0213 - PR2-EQ-0213 lines 2665-2669 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0214 - PR2-EQ-0214 lines 2671-2675 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0215 - PR2-EQ-0215 lines 2677-2687 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0216 - PR2-EQ-0216 lines 2719-2723 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0217 - PR2-EQ-0217 lines 2727-2729 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0218 - PR2-EQ-0218 lines 2733-2735 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0219 - PR2-EQ-0219 lines 2739-2745 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0220 - PR2-EQ-0220 lines 2747-2749 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0221 - PR2-EQ-0221 lines 2759-2761 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0222 - PR2-EQ-0222 lines 2763-2765 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0223 - PR2-EQ-0223 lines 2773-2785 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0224 - PR2-EQ-0224 lines 2788-2797 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0225 - PR2-EQ-0225 lines 2799-2805 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0226 - PR2-EQ-0226 lines 2811-2819 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0227 - PR2-EQ-0227 lines 2821-2835 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0228 - PR2-EQ-0228 lines 2837-2845 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0229 - PR2-EQ-0229 lines 2847-2861 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0230 - PR2-EQ-0230 lines 2863-2869 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0231 - PR2-EQ-0231 lines 2871-2877 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0232 - PR2-EQ-0232 lines 2901-2907 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0233 - PR2-EQ-0233 lines 2913-2915 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0234 - PR2-EQ-0234 lines 2917-2928 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0235 - PR2-EQ-0235 lines 2935-2945 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0236 - PR2-EQ-0236 lines 2953-2969 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0237 - PR2-EQ-0237 lines 2975-2991 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0238 - PR2-EQ-0238 lines 3000-3004 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0239 - PR2-EQ-0239 lines 3010-3022 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0240 - PR2-EQ-0240 lines 3024-3036 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0241 - PR2-EQ-0241 lines 3038-3040 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0242 - PR2-EQ-0242 lines 3042-3044 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0243 - PR2-EQ-0243 lines 3046-3054 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0244 - PR2-EQ-0244 lines 3063-3069 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0245 - PR2-EQ-0245 lines 3083-3086 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0246 - PR2-EQ-0246 lines 3090-3092 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0247 - PR2-EQ-0247 lines 3098-3100 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0248 - PR2-EQ-0248 lines 3102-3106 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0249 - PR2-EQ-0249 lines 3115-3123 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0250 - PR2-EQ-0250 lines 3125-3131 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0251 - PR2-EQ-0251 lines 3133-3146 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0252 - PR2-EQ-0252 lines 3148-3154 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0253 - PR2-EQ-0253 lines 3156-3173 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0254 - PR2-EQ-0254 lines 3222-3234 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0255 - PR2-EQ-0255 lines 3236-3241 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0256 - PR2-EQ-0256 lines 3243-3258 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0257 - PR2-EQ-0257 lines 3260-3274 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0258 - PR2-EQ-0258 lines 3278-3287 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0259 - PR2-EQ-0259 lines 3294-3296 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0260 - PR2-EQ-0260 lines 3300-3308 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0261 - PR2-EQ-0261 lines 3310-3314 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0262 - PR2-EQ-0262 lines 3316-3324 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0263 - PR2-EQ-0263 lines 3326-3334 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0264 - PR2-EQ-0264 lines 3335-3343 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0265 - PR2-EQ-0265 lines 3345-3351 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0266 - PR2-EQ-0266 lines 3353-3357 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0267 - PR2-EQ-0267 lines 3359-3367 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0268 - PR2-EQ-0268 lines 3370-3376 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0269 - PR2-EQ-0269 lines 3378-3382 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0270 - PR2-EQ-0270 lines 3384-3402 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0271 - PR2-EQ-0271 lines 3404-3412 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0272 - PR2-EQ-0272 lines 3422-3436 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0273 - PR2-EQ-0273 lines 3440-3444 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0274 - PR2-EQ-0274 lines 3446-3456 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0275 - PR2-EQ-0275 lines 3459-3469 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0276 - PR2-EQ-0276 lines 3471-3479 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0277 - PR2-EQ-0277 lines 3482-3492 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0278 - PR2-EQ-0278 lines 3494-3504 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0279 - PR2-EQ-0279 lines 3507-3517 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0280 - PR2-EQ-0280 lines 3519-3529 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0281 - PR2-EQ-0281 lines 3532-3542 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0282 - PR2-EQ-0282 lines 3544-3552 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0283 - PR2-EQ-0283 lines 3558-3560 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0284 - PR2-EQ-0284 lines 3562-3570 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0285 - PR2-EQ-0285 lines 3594-3598 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0286 - PR2-EQ-0286 lines 3623-3631 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0287 - PR2-EQ-0287 lines 3633-3641 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0288 - PR2-EQ-0288 lines 3643-3647 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0289 - PR2-EQ-0289 lines 3650-3656 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0290 - PR2-EQ-0290 lines 3658-3664 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0291 - PR2-EQ-0291 lines 3666-3672 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0292 - PR2-EQ-0292 lines 3674-3680 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0293 - PR2-EQ-0293 lines 3689-3693 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0294 - PR2-EQ-0294 lines 3696-3709 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0295 - PR2-EQ-0295 lines 3712-3722 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0296 - PR2-EQ-0296 lines 3725-3741 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0297 - PR2-EQ-0297 lines 3749-3751 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0298 - PR2-EQ-0298 lines 3755-3757 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0299 - PR2-EQ-0299 lines 3761-3763 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0300 - PR2-EQ-0300 lines 3767-3773 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0301 - PR2-EQ-0301 lines 3777-3781 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0302 - PR2-EQ-0302 lines 3793-3795 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0303 - PR2-EQ-0303 lines 3802-3808 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0304 - PR2-EQ-0304 lines 3810-3814 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0305 - PR2-EQ-0305 lines 3816-3822 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0306 - PR2-EQ-0306 lines 3825-3835 status MANUSCRIPT mode paper-cleanup

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0307 - PR2-EQ-0307 lines 3838-3849 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0308 - PR2-EQ-0308 lines 3851-3857 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0309 - PR2-EQ-0309 lines 3859-3863 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0310 - PR2-EQ-0310 lines 3869-3873 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0311 - PR2-EQ-0311 lines 3875-3885 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0312 - PR2-EQ-0312 lines 3887-3902 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0313 - PR2-EQ-0313 lines 3904-3912 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0314 - PR2-EQ-0314 lines 3914-3936 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0315 - PR2-EQ-0315 lines 3943-3949 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0316 - PR2-EQ-0316 lines 3951-3955 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0317 - PR2-EQ-0317 lines 3957-3963 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0318 - PR2-EQ-0318 lines 3965-3971 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0319 - PR2-EQ-0319 lines 3974-3980 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0320 - PR2-EQ-0320 lines 3982-3991 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0321 - PR2-EQ-0321 lines 3993-4004 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0322 - PR2-EQ-0322 lines 4006-4010 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0323 - PR2-EQ-0323 lines 4012-4018 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0324 - PR2-EQ-0324 lines 4021-4033 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0325 - PR2-EQ-0325 lines 4038-4042 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0326 - PR2-EQ-0326 lines 4044-4050 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0327 - PR2-EQ-0327 lines 4080-4093 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0328 - PR2-EQ-0328 lines 4099-4110 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0329 - PR2-EQ-0329 lines 4114-4120 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0330 - PR2-EQ-0330 lines 4122-4128 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0331 - PR2-EQ-0331 lines 4130-4144 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0332 - PR2-EQ-0332 lines 4146-4164 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0333 - PR2-EQ-0333 lines 4170-4174 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0334 - PR2-EQ-0334 lines 4183-4185 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0335 - PR2-EQ-0335 lines 4187-4189 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0336 - PR2-EQ-0336 lines 4192-4196 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0337 - PR2-EQ-0337 lines 4200-4207 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0338 - PR2-EQ-0338 lines 4211-4217 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0339 - PR2-EQ-0339 lines 4224-4234 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0340 - PR2-EQ-0340 lines 4244-4252 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0341 - PR2-EQ-0341 lines 4254-4264 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0342 - PR2-EQ-0342 lines 4266-4270 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0343 - PR2-EQ-0343 lines 4272-4284 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0344 - PR2-EQ-0344 lines 4290-4298 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0345 - PR2-EQ-0345 lines 4300-4306 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0346 - PR2-EQ-0346 lines 4311-4325 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0347 - PR2-EQ-0347 lines 4330-4342 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0348 - PR2-EQ-0348 lines 4344-4354 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0349 - PR2-EQ-0349 lines 4356-4358 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0350 - PR2-EQ-0350 lines 4360-4370 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0351 - PR2-EQ-0351 lines 4372-4378 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0352 - PR2-EQ-0352 lines 4380-4392 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0353 - PR2-EQ-0353 lines 4394-4398 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0354 - PR2-EQ-0354 lines 4400-4411 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0355 - PR2-EQ-0355 lines 4418-4422 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0356 - PR2-EQ-0356 lines 4424-4430 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0357 - PR2-EQ-0357 lines 4433-4441 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0358 - PR2-EQ-0358 lines 4443-4449 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0359 - PR2-EQ-0359 lines 4452-4465 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0360 - PR2-EQ-0360 lines 4467-4473 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0361 - PR2-EQ-0361 lines 4476-4486 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0362 - PR2-EQ-0362 lines 4494-4498 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0363 - PR2-EQ-0363 lines 4500-4508 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0364 - PR2-EQ-0364 lines 4551-4553 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0365 - PR2-EQ-0365 lines 4555-4557 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0366 - PR2-EQ-0366 lines 4560-4566 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0367 - PR2-EQ-0367 lines 4568-4579 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0368 - PR2-EQ-0368 lines 4582-4588 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0369 - PR2-EQ-0369 lines 4590-4592 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0370 - PR2-EQ-0370 lines 4594-4600 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0371 - PR2-EQ-0371 lines 4607-4618 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0372 - PR2-EQ-0372 lines 4620-4626 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0373 - PR2-EQ-0373 lines 4629-4638 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0374 - PR2-EQ-0374 lines 4640-4646 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0375 - PR2-EQ-0375 lines 4649-4660 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0376 - PR2-EQ-0376 lines 4662-4668 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0377 - PR2-EQ-0377 lines 4678-4692 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0378 - PR2-EQ-0378 lines 4747-4768 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0379 - PR2-EQ-0379 lines 4774-4786 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0380 - PR2-EQ-0380 lines 4788-4792 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0381 - PR2-EQ-0381 lines 4802-4804 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0382 - PR2-EQ-0382 lines 4810-4816 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0383 - PR2-EQ-0383 lines 4820-4824 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0384 - PR2-EQ-0384 lines 4826-4834 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0385 - PR2-EQ-0385 lines 4842-4854 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0386 - PR2-EQ-0386 lines 4856-4860 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0387 - PR2-EQ-0387 lines 4872-4887 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0388 - PR2-EQ-0388 lines 4893-4899 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0389 - PR2-EQ-0389 lines 4902-4915 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0390 - PR2-EQ-0390 lines 4918-4930 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0391 - PR2-EQ-0391 lines 4933-4945 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0392 - PR2-EQ-0392 lines 4948-4960 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0393 - PR2-EQ-0393 lines 4980-4990 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0394 - PR2-EQ-0394 lines 4992-5001 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0395 - PR2-EQ-0395 lines 5003-5009 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0396 - PR2-EQ-0396 lines 5055-5061 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0397 - PR2-EQ-0397 lines 5064-5068 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0398 - PR2-EQ-0398 lines 5070-5082 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0399 - PR2-EQ-0399 lines 5085-5089 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0400 - PR2-EQ-0400 lines 5091-5103 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0401 - PR2-EQ-0401 lines 5106-5114 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0402 - PR2-EQ-0402 lines 5116-5128 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0403 - PR2-EQ-0403 lines 5131-5137 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0404 - PR2-EQ-0404 lines 5139-5147 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0405 - PR2-EQ-0405 lines 5150-5160 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0406 - PR2-EQ-0406 lines 5162-5171 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0407 - PR2-EQ-0407 lines 5173-5179 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0408 - PR2-EQ-0408 lines 5222-5224 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0409 - PR2-EQ-0409 lines 5226-5236 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0410 - PR2-EQ-0410 lines 5238-5248 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0411 - PR2-EQ-0411 lines 5256-5260 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0412 - PR2-EQ-0412 lines 5267-5269 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0413 - PR2-EQ-0413 lines 5271-5280 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0414 - PR2-EQ-0414 lines 5287-5291 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0415 - PR2-EQ-0415 lines 5294-5300 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0416 - PR2-EQ-0416 lines 5320-5324 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0417 - PR2-EQ-0417 lines 5326-5330 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0418 - PR2-EQ-0418 lines 5332-5336 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0419 - PR2-EQ-0419 lines 5338-5353 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0420 - PR2-EQ-0420 lines 5355-5361 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0421 - PR2-EQ-0421 lines 5363-5371 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0422 - PR2-EQ-0422 lines 5373-5383 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0423 - PR2-EQ-0423 lines 5385-5394 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0424 - PR2-EQ-0424 lines 5400-5402 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0425 - PR2-EQ-0425 lines 5405-5407 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0426 - PR2-EQ-0426 lines 5409-5419 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0427 - PR2-EQ-0427 lines 5421-5431 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0428 - PR2-EQ-0428 lines 5433-5443 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0429 - PR2-EQ-0429 lines 5445-5455 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0430 - PR2-EQ-0430 lines 5458-5464 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0431 - PR2-EQ-0431 lines 5466-5472 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0432 - PR2-EQ-0432 lines 5520-5528 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0433 - PR2-EQ-0433 lines 5531-5535 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0434 - PR2-EQ-0434 lines 5539-5545 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0435 - PR2-EQ-0435 lines 5548-5560 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0436 - PR2-EQ-0436 lines 5569-5573 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0437 - PR2-EQ-0437 lines 5575-5585 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0438 - PR2-EQ-0438 lines 5588-5598 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0439 - PR2-EQ-0439 lines 5601-5607 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0440 - PR2-EQ-0440 lines 5610-5618 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0441 - PR2-EQ-0441 lines 5621-5627 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0442 - PR2-EQ-0442 lines 5635-5648 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0443 - PR2-EQ-0443 lines 5651-5659 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0444 - PR2-EQ-0444 lines 5671-5673 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0445 - PR2-EQ-0445 lines 5706-5713 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0446 - PR2-EQ-0446 lines 6449-6453 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-PASS-COUNT - Display blocks with Maple-backed PASS coverage

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `271.`
- expected: `271.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-NOTE-COUNT - Display blocks with explicit NOTE coverage

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `111.`
- expected: `111.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-DATA-COUNT - Display blocks with explicit DATA coverage

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `62.`
- expected: `62.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-MANUSCRIPT-COUNT - Display blocks flagged as manuscript cleanup

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `2.`
- expected: `2.`
- residual_or_error: `0.`
- tolerance: `0.`

