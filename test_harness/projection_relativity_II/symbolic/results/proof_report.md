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
- actual: `44354.`
- expected: `\label{sec:pr2_weak_mixing_boundary_closure}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC002 - Weak mixing numeric target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `45296.`
- expected: `0.231355763298189`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC003 - Generated weak scale target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `61991.`
- expected: `246.21959589022453`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC004 - Fermi constant target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `62173.`
- expected: `1.166379220175995`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC005 - Anomaly section label present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `97888.`
- expected: `\label{sec:pr2_fermion_representation_anomaly_cancellation}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC006 - Charged-lepton section label present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `132083.`
- expected: `\label{sec:pr2_charged_lepton_precision_candidate}`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC007 - Electron candidate target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `139750.`
- expected: `0.510984463`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC008 - Strong-coupling target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `149285.`
- expected: `0.117861507469150`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC009 - QCD Lambda_6 target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `156625.`
- expected: `0.08776758507426047`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC010 - CKM Jarlskog target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `173729.`
- expected: `3.152605677`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC011 - PMNS Jarlskog target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `178317.`
- expected: `-8.935540`
- residual_or_error: `0.`
- tolerance: `0.`

## SRC012 - m_beta_beta target present

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: source-text
- actual: `194529.`
- expected: `1.507694477`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-DISPLAY-COUNT - Every top-level display block is inventoried

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `442.`
- expected: `442.`
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

## LATEX-PR2-EQ-0002 - PR2-EQ-0002 lines 84-92 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0003 - PR2-EQ-0003 lines 94-98 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0004 - PR2-EQ-0004 lines 105-109 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0005 - PR2-EQ-0005 lines 111-119 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0006 - PR2-EQ-0006 lines 123-133 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0007 - PR2-EQ-0007 lines 135-145 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0008 - PR2-EQ-0008 lines 156-162 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0009 - PR2-EQ-0009 lines 164-170 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0010 - PR2-EQ-0010 lines 174-189 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0011 - PR2-EQ-0011 lines 198-200 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0012 - PR2-EQ-0012 lines 229-235 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0013 - PR2-EQ-0013 lines 238-244 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0014 - PR2-EQ-0014 lines 247-251 status PASS mode section-chain

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

## LATEX-PR2-EQ-0016 - PR2-EQ-0016 lines 258-260 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0017 - PR2-EQ-0017 lines 263-271 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0018 - PR2-EQ-0018 lines 275-281 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0019 - PR2-EQ-0019 lines 283-291 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0020 - PR2-EQ-0020 lines 293-301 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0021 - PR2-EQ-0021 lines 344-354 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0022 - PR2-EQ-0022 lines 358-368 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0023 - PR2-EQ-0023 lines 370-372 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0024 - PR2-EQ-0024 lines 374-381 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0025 - PR2-EQ-0025 lines 383-390 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0026 - PR2-EQ-0026 lines 393-397 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0027 - PR2-EQ-0027 lines 399-405 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0028 - PR2-EQ-0028 lines 408-415 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0029 - PR2-EQ-0029 lines 417-423 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0030 - PR2-EQ-0030 lines 475-481 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0031 - PR2-EQ-0031 lines 483-489 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0032 - PR2-EQ-0032 lines 493-500 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0033 - PR2-EQ-0033 lines 502-509 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0034 - PR2-EQ-0034 lines 564-574 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0035 - PR2-EQ-0035 lines 582-588 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0036 - PR2-EQ-0036 lines 590-596 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0037 - PR2-EQ-0037 lines 598-602 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0038 - PR2-EQ-0038 lines 605-610 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0039 - PR2-EQ-0039 lines 613-617 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0040 - PR2-EQ-0040 lines 619-625 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0041 - PR2-EQ-0041 lines 631-635 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0042 - PR2-EQ-0042 lines 638-642 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0043 - PR2-EQ-0043 lines 644-650 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0044 - PR2-EQ-0044 lines 653-659 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0045 - PR2-EQ-0045 lines 661-671 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0046 - PR2-EQ-0046 lines 677-682 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0047 - PR2-EQ-0047 lines 684-689 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0048 - PR2-EQ-0048 lines 691-697 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0049 - PR2-EQ-0049 lines 699-707 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0050 - PR2-EQ-0050 lines 716-720 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0051 - PR2-EQ-0051 lines 722-736 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0052 - PR2-EQ-0052 lines 738-748 status PASS mode direct-symbolic

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

## LATEX-PR2-EQ-0054 - PR2-EQ-0054 lines 759-761 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0055 - PR2-EQ-0055 lines 763-770 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0056 - PR2-EQ-0056 lines 772-781 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0057 - PR2-EQ-0057 lines 783-791 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0058 - PR2-EQ-0058 lines 794-800 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0059 - PR2-EQ-0059 lines 806-817 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0060 - PR2-EQ-0060 lines 821-827 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0061 - PR2-EQ-0061 lines 835-837 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0062 - PR2-EQ-0062 lines 840-846 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0063 - PR2-EQ-0063 lines 848-854 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0064 - PR2-EQ-0064 lines 930-940 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0065 - PR2-EQ-0065 lines 942-954 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0066 - PR2-EQ-0066 lines 956-966 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0067 - PR2-EQ-0067 lines 969-975 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0068 - PR2-EQ-0068 lines 985-988 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0069 - PR2-EQ-0069 lines 991-1000 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0070 - PR2-EQ-0070 lines 1002-1006 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0071 - PR2-EQ-0071 lines 1008-1016 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0072 - PR2-EQ-0072 lines 1018-1024 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0073 - PR2-EQ-0073 lines 1027-1038 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0074 - PR2-EQ-0074 lines 1044-1056 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0075 - PR2-EQ-0075 lines 1058-1062 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0076 - PR2-EQ-0076 lines 1064-1074 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0077 - PR2-EQ-0077 lines 1083-1085 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0078 - PR2-EQ-0078 lines 1087-1093 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0079 - PR2-EQ-0079 lines 1095-1097 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0080 - PR2-EQ-0080 lines 1104-1106 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0081 - PR2-EQ-0081 lines 1109-1113 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0082 - PR2-EQ-0082 lines 1115-1121 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0083 - PR2-EQ-0083 lines 1124-1130 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0084 - PR2-EQ-0084 lines 1132-1140 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0085 - PR2-EQ-0085 lines 1142-1148 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0086 - PR2-EQ-0086 lines 1150-1156 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0087 - PR2-EQ-0087 lines 1158-1166 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0088 - PR2-EQ-0088 lines 1176-1187 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0089 - PR2-EQ-0089 lines 1189-1193 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0090 - PR2-EQ-0090 lines 1195-1206 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0091 - PR2-EQ-0091 lines 1208-1212 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0092 - PR2-EQ-0092 lines 1214-1218 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0093 - PR2-EQ-0093 lines 1221-1229 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0094 - PR2-EQ-0094 lines 1235-1246 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0095 - PR2-EQ-0095 lines 1248-1262 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0096 - PR2-EQ-0096 lines 1264-1280 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0097 - PR2-EQ-0097 lines 1286-1294 status DATA mode boundary

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

## LATEX-PR2-EQ-0099 - PR2-EQ-0099 lines 1301-1303 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0100 - PR2-EQ-0100 lines 1305-1311 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0101 - PR2-EQ-0101 lines 1317-1321 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0102 - PR2-EQ-0102 lines 1323-1328 status NOTE mode context

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0103 - PR2-EQ-0103 lines 1389-1391 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0104 - PR2-EQ-0104 lines 1393-1397 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0105 - PR2-EQ-0105 lines 1399-1403 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0106 - PR2-EQ-0106 lines 1405-1413 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0107 - PR2-EQ-0107 lines 1421-1426 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0108 - PR2-EQ-0108 lines 1428-1436 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0109 - PR2-EQ-0109 lines 1438-1444 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0110 - PR2-EQ-0110 lines 1447-1453 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0111 - PR2-EQ-0111 lines 1455-1461 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0112 - PR2-EQ-0112 lines 1464-1471 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0113 - PR2-EQ-0113 lines 1478-1480 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0114 - PR2-EQ-0114 lines 1482-1492 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0115 - PR2-EQ-0115 lines 1494-1500 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0116 - PR2-EQ-0116 lines 1502-1510 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0117 - PR2-EQ-0117 lines 1514-1518 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0118 - PR2-EQ-0118 lines 1525-1535 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0119 - PR2-EQ-0119 lines 1537-1545 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0120 - PR2-EQ-0120 lines 1548-1567 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0121 - PR2-EQ-0121 lines 1573-1579 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0122 - PR2-EQ-0122 lines 1582-1590 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0123 - PR2-EQ-0123 lines 1592-1596 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0124 - PR2-EQ-0124 lines 1599-1607 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0125 - PR2-EQ-0125 lines 1609-1615 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0126 - PR2-EQ-0126 lines 1617-1623 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0127 - PR2-EQ-0127 lines 1626-1638 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0128 - PR2-EQ-0128 lines 1643-1648 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0129 - PR2-EQ-0129 lines 1650-1656 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0130 - PR2-EQ-0130 lines 1658-1671 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0131 - PR2-EQ-0131 lines 1674-1678 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0132 - PR2-EQ-0132 lines 1680-1692 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0133 - PR2-EQ-0133 lines 1694-1706 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0134 - PR2-EQ-0134 lines 1746-1752 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0135 - PR2-EQ-0135 lines 1754-1763 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0136 - PR2-EQ-0136 lines 1765-1777 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0137 - PR2-EQ-0137 lines 1781-1787 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0138 - PR2-EQ-0138 lines 1789-1795 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0139 - PR2-EQ-0139 lines 1802-1818 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0140 - PR2-EQ-0140 lines 1820-1832 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0141 - PR2-EQ-0141 lines 1834-1854 status DATA mode boundary

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

## LATEX-PR2-EQ-0143 - PR2-EQ-0143 lines 1865-1867 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0144 - PR2-EQ-0144 lines 1869-1881 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0145 - PR2-EQ-0145 lines 1888-1893 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0146 - PR2-EQ-0146 lines 1895-1900 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0147 - PR2-EQ-0147 lines 1902-1908 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0148 - PR2-EQ-0148 lines 1917-1927 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0149 - PR2-EQ-0149 lines 1929-1940 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0150 - PR2-EQ-0150 lines 1942-1949 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0151 - PR2-EQ-0151 lines 1951-1957 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0152 - PR2-EQ-0152 lines 1959-1972 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0153 - PR2-EQ-0153 lines 1976-1980 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0154 - PR2-EQ-0154 lines 1986-1990 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0155 - PR2-EQ-0155 lines 1992-1994 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0156 - PR2-EQ-0156 lines 1996-2004 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0157 - PR2-EQ-0157 lines 2006-2014 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0158 - PR2-EQ-0158 lines 2016-2025 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0159 - PR2-EQ-0159 lines 2027-2037 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0160 - PR2-EQ-0160 lines 2039-2049 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0161 - PR2-EQ-0161 lines 2052-2064 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0162 - PR2-EQ-0162 lines 2073-2080 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0163 - PR2-EQ-0163 lines 2083-2090 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0164 - PR2-EQ-0164 lines 2092-2098 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0165 - PR2-EQ-0165 lines 2100-2114 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0166 - PR2-EQ-0166 lines 2116-2126 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0167 - PR2-EQ-0167 lines 2134-2140 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0168 - PR2-EQ-0168 lines 2143-2155 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0169 - PR2-EQ-0169 lines 2165-2173 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0170 - PR2-EQ-0170 lines 2175-2179 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0171 - PR2-EQ-0171 lines 2188-2194 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0172 - PR2-EQ-0172 lines 2195-2205 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0173 - PR2-EQ-0173 lines 2206-2214 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0174 - PR2-EQ-0174 lines 2216-2224 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0175 - PR2-EQ-0175 lines 2226-2239 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0176 - PR2-EQ-0176 lines 2248-2256 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0177 - PR2-EQ-0177 lines 2260-2262 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0178 - PR2-EQ-0178 lines 2266-2274 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0179 - PR2-EQ-0179 lines 2278-2282 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0180 - PR2-EQ-0180 lines 2284-2291 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0181 - PR2-EQ-0181 lines 2294-2298 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0182 - PR2-EQ-0182 lines 2305-2315 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0183 - PR2-EQ-0183 lines 2322-2326 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0184 - PR2-EQ-0184 lines 2328-2342 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0185 - PR2-EQ-0185 lines 2344-2354 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0186 - PR2-EQ-0186 lines 2356-2362 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0187 - PR2-EQ-0187 lines 2364-2368 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0188 - PR2-EQ-0188 lines 2370-2374 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0189 - PR2-EQ-0189 lines 2376-2380 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0190 - PR2-EQ-0190 lines 2382-2388 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0191 - PR2-EQ-0191 lines 2390-2396 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0192 - PR2-EQ-0192 lines 2398-2404 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0193 - PR2-EQ-0193 lines 2407-2415 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0194 - PR2-EQ-0194 lines 2420-2428 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0195 - PR2-EQ-0195 lines 2430-2439 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0196 - PR2-EQ-0196 lines 2443-2450 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0197 - PR2-EQ-0197 lines 2452-2456 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0198 - PR2-EQ-0198 lines 2458-2462 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0199 - PR2-EQ-0199 lines 2464-2470 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0200 - PR2-EQ-0200 lines 2472-2478 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0201 - PR2-EQ-0201 lines 2480-2486 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0202 - PR2-EQ-0202 lines 2492-2504 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0203 - PR2-EQ-0203 lines 2507-2518 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0204 - PR2-EQ-0204 lines 2521-2529 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0205 - PR2-EQ-0205 lines 2531-2537 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0206 - PR2-EQ-0206 lines 2540-2555 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0207 - PR2-EQ-0207 lines 2557-2571 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0208 - PR2-EQ-0208 lines 2574-2580 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0209 - PR2-EQ-0209 lines 2582-2586 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0210 - PR2-EQ-0210 lines 2588-2596 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0211 - PR2-EQ-0211 lines 2602-2608 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0212 - PR2-EQ-0212 lines 2610-2620 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0213 - PR2-EQ-0213 lines 2661-2667 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0214 - PR2-EQ-0214 lines 2669-2673 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0215 - PR2-EQ-0215 lines 2675-2679 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0216 - PR2-EQ-0216 lines 2681-2691 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0217 - PR2-EQ-0217 lines 2723-2727 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0218 - PR2-EQ-0218 lines 2731-2733 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0219 - PR2-EQ-0219 lines 2737-2739 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0220 - PR2-EQ-0220 lines 2743-2749 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0221 - PR2-EQ-0221 lines 2751-2753 status DATA mode boundary

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

## LATEX-PR2-EQ-0223 - PR2-EQ-0223 lines 2767-2769 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0224 - PR2-EQ-0224 lines 2777-2789 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0225 - PR2-EQ-0225 lines 2792-2801 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0226 - PR2-EQ-0226 lines 2803-2809 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0227 - PR2-EQ-0227 lines 2815-2823 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0228 - PR2-EQ-0228 lines 2825-2839 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0229 - PR2-EQ-0229 lines 2841-2849 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0230 - PR2-EQ-0230 lines 2851-2865 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0231 - PR2-EQ-0231 lines 2867-2873 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0232 - PR2-EQ-0232 lines 2875-2881 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0233 - PR2-EQ-0233 lines 2905-2911 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0234 - PR2-EQ-0234 lines 2917-2919 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0235 - PR2-EQ-0235 lines 2921-2932 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0236 - PR2-EQ-0236 lines 2939-2949 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0237 - PR2-EQ-0237 lines 2957-2973 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0238 - PR2-EQ-0238 lines 2979-2995 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0239 - PR2-EQ-0239 lines 3004-3008 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0240 - PR2-EQ-0240 lines 3014-3026 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0241 - PR2-EQ-0241 lines 3028-3040 status NOTE mode note-boundary

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

## LATEX-PR2-EQ-0243 - PR2-EQ-0243 lines 3046-3048 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0244 - PR2-EQ-0244 lines 3050-3058 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0245 - PR2-EQ-0245 lines 3067-3073 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0246 - PR2-EQ-0246 lines 3087-3090 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0247 - PR2-EQ-0247 lines 3094-3096 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0248 - PR2-EQ-0248 lines 3102-3104 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0249 - PR2-EQ-0249 lines 3106-3110 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0250 - PR2-EQ-0250 lines 3119-3127 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0251 - PR2-EQ-0251 lines 3129-3135 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0252 - PR2-EQ-0252 lines 3137-3150 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0253 - PR2-EQ-0253 lines 3152-3158 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0254 - PR2-EQ-0254 lines 3160-3177 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0255 - PR2-EQ-0255 lines 3226-3238 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0256 - PR2-EQ-0256 lines 3240-3245 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0257 - PR2-EQ-0257 lines 3247-3262 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0258 - PR2-EQ-0258 lines 3264-3278 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0259 - PR2-EQ-0259 lines 3282-3291 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0260 - PR2-EQ-0260 lines 3298-3300 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0261 - PR2-EQ-0261 lines 3304-3312 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0262 - PR2-EQ-0262 lines 3314-3318 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0263 - PR2-EQ-0263 lines 3320-3328 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0264 - PR2-EQ-0264 lines 3330-3338 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0265 - PR2-EQ-0265 lines 3339-3347 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0266 - PR2-EQ-0266 lines 3349-3355 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0267 - PR2-EQ-0267 lines 3357-3361 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0268 - PR2-EQ-0268 lines 3363-3371 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0269 - PR2-EQ-0269 lines 3374-3380 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0270 - PR2-EQ-0270 lines 3382-3386 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0271 - PR2-EQ-0271 lines 3388-3406 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0272 - PR2-EQ-0272 lines 3408-3416 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0273 - PR2-EQ-0273 lines 3426-3440 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0274 - PR2-EQ-0274 lines 3444-3448 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0275 - PR2-EQ-0275 lines 3450-3460 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0276 - PR2-EQ-0276 lines 3463-3473 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0277 - PR2-EQ-0277 lines 3475-3483 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0278 - PR2-EQ-0278 lines 3486-3496 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0279 - PR2-EQ-0279 lines 3498-3508 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0280 - PR2-EQ-0280 lines 3511-3521 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0281 - PR2-EQ-0281 lines 3523-3533 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0282 - PR2-EQ-0282 lines 3536-3546 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0283 - PR2-EQ-0283 lines 3548-3556 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0284 - PR2-EQ-0284 lines 3562-3564 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0285 - PR2-EQ-0285 lines 3566-3574 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0286 - PR2-EQ-0286 lines 3598-3602 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0287 - PR2-EQ-0287 lines 3627-3635 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0288 - PR2-EQ-0288 lines 3637-3645 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0289 - PR2-EQ-0289 lines 3647-3651 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0290 - PR2-EQ-0290 lines 3654-3660 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0291 - PR2-EQ-0291 lines 3662-3668 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0292 - PR2-EQ-0292 lines 3670-3676 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0293 - PR2-EQ-0293 lines 3678-3684 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0294 - PR2-EQ-0294 lines 3693-3697 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0295 - PR2-EQ-0295 lines 3700-3713 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0296 - PR2-EQ-0296 lines 3716-3726 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0297 - PR2-EQ-0297 lines 3729-3745 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0298 - PR2-EQ-0298 lines 3753-3755 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0299 - PR2-EQ-0299 lines 3759-3761 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0300 - PR2-EQ-0300 lines 3765-3767 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0301 - PR2-EQ-0301 lines 3771-3777 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0302 - PR2-EQ-0302 lines 3781-3785 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0303 - PR2-EQ-0303 lines 3797-3799 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0304 - PR2-EQ-0304 lines 3805-3813 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0305 - PR2-EQ-0305 lines 3815-3826 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0306 - PR2-EQ-0306 lines 3828-3834 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0307 - PR2-EQ-0307 lines 3836-3840 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0308 - PR2-EQ-0308 lines 3846-3850 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0309 - PR2-EQ-0309 lines 3852-3862 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0310 - PR2-EQ-0310 lines 3864-3879 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0311 - PR2-EQ-0311 lines 3881-3889 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0312 - PR2-EQ-0312 lines 3891-3913 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0313 - PR2-EQ-0313 lines 3920-3926 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0314 - PR2-EQ-0314 lines 3928-3932 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0315 - PR2-EQ-0315 lines 3934-3940 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0316 - PR2-EQ-0316 lines 3942-3948 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0317 - PR2-EQ-0317 lines 3951-3957 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0318 - PR2-EQ-0318 lines 3959-3968 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0319 - PR2-EQ-0319 lines 3970-3981 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0320 - PR2-EQ-0320 lines 3983-3987 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0321 - PR2-EQ-0321 lines 3989-3995 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0322 - PR2-EQ-0322 lines 3998-4010 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0323 - PR2-EQ-0323 lines 4015-4019 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0324 - PR2-EQ-0324 lines 4021-4027 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0325 - PR2-EQ-0325 lines 4057-4070 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0326 - PR2-EQ-0326 lines 4076-4087 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0327 - PR2-EQ-0327 lines 4091-4097 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0328 - PR2-EQ-0328 lines 4099-4105 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0329 - PR2-EQ-0329 lines 4107-4121 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0330 - PR2-EQ-0330 lines 4123-4141 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0331 - PR2-EQ-0331 lines 4147-4151 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0332 - PR2-EQ-0332 lines 4160-4162 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0333 - PR2-EQ-0333 lines 4164-4166 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0334 - PR2-EQ-0334 lines 4169-4173 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0335 - PR2-EQ-0335 lines 4177-4184 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0336 - PR2-EQ-0336 lines 4188-4194 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0337 - PR2-EQ-0337 lines 4201-4211 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0338 - PR2-EQ-0338 lines 4221-4229 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0339 - PR2-EQ-0339 lines 4231-4241 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0340 - PR2-EQ-0340 lines 4243-4247 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0341 - PR2-EQ-0341 lines 4249-4261 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0342 - PR2-EQ-0342 lines 4267-4275 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0343 - PR2-EQ-0343 lines 4277-4283 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0344 - PR2-EQ-0344 lines 4288-4302 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0345 - PR2-EQ-0345 lines 4307-4319 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0346 - PR2-EQ-0346 lines 4321-4331 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0347 - PR2-EQ-0347 lines 4333-4335 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0348 - PR2-EQ-0348 lines 4337-4347 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0349 - PR2-EQ-0349 lines 4349-4355 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0350 - PR2-EQ-0350 lines 4357-4369 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0351 - PR2-EQ-0351 lines 4371-4375 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0352 - PR2-EQ-0352 lines 4377-4388 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0353 - PR2-EQ-0353 lines 4395-4399 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0354 - PR2-EQ-0354 lines 4401-4407 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0355 - PR2-EQ-0355 lines 4410-4418 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0356 - PR2-EQ-0356 lines 4420-4426 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0357 - PR2-EQ-0357 lines 4429-4442 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0358 - PR2-EQ-0358 lines 4444-4450 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0359 - PR2-EQ-0359 lines 4453-4463 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0360 - PR2-EQ-0360 lines 4471-4475 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0361 - PR2-EQ-0361 lines 4477-4485 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0362 - PR2-EQ-0362 lines 4529-4535 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0363 - PR2-EQ-0363 lines 4537-4548 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0364 - PR2-EQ-0364 lines 4551-4557 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0365 - PR2-EQ-0365 lines 4559-4561 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0366 - PR2-EQ-0366 lines 4563-4569 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0367 - PR2-EQ-0367 lines 4576-4587 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0368 - PR2-EQ-0368 lines 4589-4595 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0369 - PR2-EQ-0369 lines 4598-4607 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0370 - PR2-EQ-0370 lines 4609-4615 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0371 - PR2-EQ-0371 lines 4618-4629 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0372 - PR2-EQ-0372 lines 4631-4637 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0373 - PR2-EQ-0373 lines 4647-4661 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0374 - PR2-EQ-0374 lines 4716-4737 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0375 - PR2-EQ-0375 lines 4743-4755 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0376 - PR2-EQ-0376 lines 4757-4761 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0377 - PR2-EQ-0377 lines 4771-4773 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0378 - PR2-EQ-0378 lines 4779-4785 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0379 - PR2-EQ-0379 lines 4789-4793 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0380 - PR2-EQ-0380 lines 4795-4803 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0381 - PR2-EQ-0381 lines 4811-4823 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0382 - PR2-EQ-0382 lines 4825-4829 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0383 - PR2-EQ-0383 lines 4841-4856 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0384 - PR2-EQ-0384 lines 4862-4868 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0385 - PR2-EQ-0385 lines 4871-4884 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0386 - PR2-EQ-0386 lines 4887-4899 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0387 - PR2-EQ-0387 lines 4902-4914 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0388 - PR2-EQ-0388 lines 4917-4929 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0389 - PR2-EQ-0389 lines 4949-4959 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0390 - PR2-EQ-0390 lines 4961-4970 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0391 - PR2-EQ-0391 lines 4972-4978 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0392 - PR2-EQ-0392 lines 5024-5030 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0393 - PR2-EQ-0393 lines 5033-5037 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0394 - PR2-EQ-0394 lines 5039-5051 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0395 - PR2-EQ-0395 lines 5054-5058 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0396 - PR2-EQ-0396 lines 5060-5072 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0397 - PR2-EQ-0397 lines 5075-5083 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0398 - PR2-EQ-0398 lines 5085-5097 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0399 - PR2-EQ-0399 lines 5100-5106 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0400 - PR2-EQ-0400 lines 5108-5116 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0401 - PR2-EQ-0401 lines 5119-5129 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0402 - PR2-EQ-0402 lines 5131-5140 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0403 - PR2-EQ-0403 lines 5142-5148 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0404 - PR2-EQ-0404 lines 5190-5192 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0405 - PR2-EQ-0405 lines 5194-5204 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0406 - PR2-EQ-0406 lines 5206-5216 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0407 - PR2-EQ-0407 lines 5224-5228 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0408 - PR2-EQ-0408 lines 5235-5237 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0409 - PR2-EQ-0409 lines 5239-5248 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0410 - PR2-EQ-0410 lines 5255-5259 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0411 - PR2-EQ-0411 lines 5262-5268 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0412 - PR2-EQ-0412 lines 5288-5292 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0413 - PR2-EQ-0413 lines 5294-5298 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0414 - PR2-EQ-0414 lines 5300-5304 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0415 - PR2-EQ-0415 lines 5306-5321 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0416 - PR2-EQ-0416 lines 5323-5329 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0417 - PR2-EQ-0417 lines 5331-5339 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0418 - PR2-EQ-0418 lines 5341-5351 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0419 - PR2-EQ-0419 lines 5353-5362 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0420 - PR2-EQ-0420 lines 5368-5370 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0421 - PR2-EQ-0421 lines 5373-5375 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0422 - PR2-EQ-0422 lines 5377-5387 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0423 - PR2-EQ-0423 lines 5389-5399 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0424 - PR2-EQ-0424 lines 5401-5411 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0425 - PR2-EQ-0425 lines 5413-5423 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0426 - PR2-EQ-0426 lines 5426-5432 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0427 - PR2-EQ-0427 lines 5434-5440 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0428 - PR2-EQ-0428 lines 5488-5496 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0429 - PR2-EQ-0429 lines 5499-5503 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0430 - PR2-EQ-0430 lines 5507-5513 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0431 - PR2-EQ-0431 lines 5516-5528 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0432 - PR2-EQ-0432 lines 5537-5541 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0433 - PR2-EQ-0433 lines 5543-5553 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0434 - PR2-EQ-0434 lines 5556-5566 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0435 - PR2-EQ-0435 lines 5569-5575 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0436 - PR2-EQ-0436 lines 5578-5586 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0437 - PR2-EQ-0437 lines 5589-5595 status PASS mode direct-numeric

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0438 - PR2-EQ-0438 lines 5603-5616 status PASS mode direct-symbolic

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0439 - PR2-EQ-0439 lines 5619-5627 status PASS mode section-chain

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0440 - PR2-EQ-0440 lines 5639-5641 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0441 - PR2-EQ-0441 lines 5674-5681 status DATA mode boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-PR2-EQ-0442 - PR2-EQ-0442 lines 6415-6419 status NOTE mode note-boundary

- paper_location: source:all-display-blocks
- kind: predicate
- actual: `true`
- expected: `true`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-PASS-COUNT - Display blocks with Maple-backed PASS coverage

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `268.`
- expected: `268.`
- residual_or_error: `0.`
- tolerance: `0.`

## LATEX-COVERAGE-NOTE-COUNT - Display blocks with explicit NOTE coverage

- paper_location: source:Oshetski_Projection_Relativity_II_Main.tex
- kind: exact
- actual: `112.`
- expected: `112.`
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
- actual: `0.`
- expected: `0.`
- residual_or_error: `0.`
- tolerance: `0.`

