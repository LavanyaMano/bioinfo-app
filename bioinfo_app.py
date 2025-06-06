import streamlit as st
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

st.title("🔬 Simple Bioinformatics App")

st.header("Enter DNA Sequence")
sequence_input = st.text_area("Paste DNA Sequence (ATGC only)", height=150)
sequence_input = sequence_input.replace(" ", "").replace("\n", "").upper()

if sequence_input:
    try:
        dna_seq = Seq(sequence_input)

        st.subheader("📊 Nucleotide Composition")
        st.write(f"A: {dna_seq.count('A')}")
        st.write(f"T: {dna_seq.count('T')}")
        st.write(f"G: {dna_seq.count('G')}")
        st.write(f"C: {dna_seq.count('C')}")

        st.subheader("🧬 GC Content")
        st.write(f"{gc_fraction(dna_seq)*100:.2f}%")

        st.subheader("🧪 Transcription (DNA → RNA)")
        rna_seq = dna_seq.transcribe()
        st.code(rna_seq)

        st.subheader("🧬 Translation (RNA → Protein)")
        try:
            protein_seq = rna_seq.translate(to_stop=True)
            st.code(protein_seq)
        except Exception as e:
            st.error(f"Translation error: {e}")

    except Exception as e:
        st.error(f"Invalid DNA sequence: {e}")
else:
    st.info("Please enter a DNA sequence to get started.")
