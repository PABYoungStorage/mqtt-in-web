// const renderer = new THREE.WebGLRenderer();
// renderer.setSize( 100, 100);
// document.body.appendChild( renderer.domElement );

// const camera = new THREE.PerspectiveCamera( 10, window.innerWidth / window.innerHeight, 1, 1000 );
// camera.position.set( 0, 0, 300 );
// camera.lookAt( 0, 0, 0 );

// const scene = new THREE.Scene();

// //create a blue LineBasicMaterial
// const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );

// const points = [];
// points.push( new THREE.Vector3( 0, 0, 0 ) );
// points.push( new THREE.Vector3( 10, 0, 0 ) );
// points.push( new THREE.Vector3( 11, 10, 0 ) );
// points.push( new THREE.Vector3( 5, 20, 0 ) );

// const geometry = new THREE.BufferGeometry().setFromPoints( points );

// const line = new THREE.Line( geometry, material );

// scene.add( line );
// renderer.render( scene, camera );