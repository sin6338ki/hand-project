import React, { Suspense } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { Model } from "./Model";

const HandsModel = () => {
  return (
    <Canvas
      camera={{ position: [3, 0, 12.25], fov: 30 }}
      style={{
        height: "35vh",
      }}
    >
      <ambientLight intensity={1} />
      <directionalLight intensity={1} />
      <Suspense fallback={null}>
        <Model position={[0, 0, 0]} scale={[0.025, 0.025, 0.025]} />
      </Suspense>
      <OrbitControls autoRotate={true} autoRotateSpeed={10.0} />
    </Canvas>
  );
};

export default HandsModel;
