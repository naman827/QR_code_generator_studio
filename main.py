import streamlit as st
import segno
import io
import pathlib as path

icon_path=path.Path("assets/logo.png")

if icon_path.is_file():
    app_icon=str(icon_path)
else:
    app_icon="⚡"

st.set_page_config(
    page_title="Enterprise QR Code Studio",
    page_icon=app_icon,
    layout="centered"
)

st.title("Enterprise QR Code Generator")
st.markdown("Input you target configurations below to generate an instant, production-grade QR code asset")

st.sidebar.header("QR code specifications")

payload_url=st.text_input(
    "Target URL or Text Data",
    value="https://example.com",
    placeholder="Enter URL here..."
)

col1,col2=st.sidebar.columns(2)
with col1:
    scale_factor=st.number_input("Scale(Resolution)",min_value=1,max_value=50,value=10,step=1)
with col2:
    border_zone=st.number_input("Border(Quiet Zone)",min_value=4,max_value=20,value=4,step=1,help="ISO standards mandate a minimum border width of 4 modules")

st.sidebar.subheader("Color palette")
dark_color=st.sidebar.color_picker("Foreground/Dark Blocks","#000000")
light_color=st.sidebar.color_picker("Background/Canvas","#ffffff")

ecc_options={
    "Level L (7% recovery)":"L",
    "Level M(15% recovery)":"M",
    "Level Q(25% recovery)":"Q",
    "Level H(30% recovery)":"H",
}

selected_label=st.sidebar.selectbox(
    "Error Correction Coding(ECC)",
    options=list(ecc_options.keys()),
    index=1,
    help="Higher levels withstand more physical damage or distribution,useful if adding overlay graphics"
)

clean_ecc=ecc_options[selected_label]

if not payload_url.strip():
    st.warning("Please provide a valid URL or text payload to compile the QR matrix.")
else:
    try:
        qr=segno.make_qr(payload_url,error=clean_ecc)

        img_buffer=io.BytesIO()
        qr.save(
            img_buffer,
            kind='png',
            scale=scale_factor,
            border=border_zone,
            dark=dark_color,
            light=light_color
        )
        img_bytes=img_buffer.getvalue()

        st.subheader("Generated Output Viewport")

        st.image(img_bytes,caption=f"Matrix Version:{qr.version} | Mode:{qr.mode}",use_container_width=False)

        st.download_button(
            label="download asset (.png)",
            data = img_bytes,
            file_name="Production_qr.png",
            mime="image/png"
        )

        with st.expander("view code structural telementry"):
                st.json({
                    "Matrix Version":qr.version,
                    "Encoding Mode":qr.mode,
                    "ECC Level Target":clean_ecc,
                    "Scale Factor Multiplier":scale_factor,
                    "Quiet Zone Size(Border)":border_zone,
                    "Hex Mapping":{"dark":dark_color,"light":light_color}
            })

    except Exception as e:
        st.error(f"failsafe triggered. Compilation failed:{str(e)}")
