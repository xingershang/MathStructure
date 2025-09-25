<goal>
Prove that for any sets A and B, A × ⋃B = ⋃{A × X ∣ X ∈ B}.
</goal>

<sufficiency_proof>
First, we prove the (⊆) direction. Let (a, x) ∈ A × ⋃B. By definition, x ∈ ⋃B, so there exists X ∈ B such that x ∈ X. Therefore, (a, x) ∈ A × X. Since A × X is part of the union ⋃{A × X ∣ X ∈ B}, we conclude (a, x) ∈ ⋃{A × X ∣ X ∈ B}.
</sufficiency_proof>

<necessity_proof>
Next, we prove the (⊇) direction. Let (a, x) ∈ ⋃{A × X ∣ X ∈ B}. Then there exists X ∈ B such that (a, x) ∈ A × X. By definition of Cartesian product, a ∈ A and x ∈ X. Since X ∈ B, we have x ∈ ⋃B. Thus, (a, x) ∈ A × ⋃B.
</necessity_proof>

<conclusion>
Hence, the equality A × ⋃B = ⋃{A × X ∣ X ∈ B} holds.
</conclusion>
