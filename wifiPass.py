import argparse
import tempfile
import qrcode
from fpdf import FPDF

if __name__ == "__main__":
    file_format = ["PNG", "PDF", "BOTH"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--ssid', required=True)
    parser.add_argument('--pw', required=True)
    parser.add_argument('--format', required=True, choices=file_format)
    parser.add_argument('--out', required=False)
    args = parser.parse_args()


    use_format = args.format
    ssid = args.ssid
    pw = args.pw
    if args.out:
        out_name = args.out
    else:
        out_name = f"wifiPass_{ssid}"

    img = qrcode.make(f'WIFI:T:WPA;S:{ssid};P:{pw};;')
    pdf = FPDF()
    pdf.add_page(orientation="P")

    if use_format == "PNG":
        img.save(f"{out_name}.png", format="PNG")
    elif use_format == "PDF":
        fp = tempfile.NamedTemporaryFile()
        img.save(fp, format="PNG")
        pdf.set_font("Arial", "", 14)
        pdf.write(5, f"SSID: {ssid}\nPW: {pw}\n")
        pdf.image(fp.name, 0, None, 200, 200, type="PNG")
        pdf.output(f"{out_name}.pdf")
        fp.close()
    elif use_format == "BOTH":
        img.save(f"{out_name}.png", format="PNG")
        pdf.set_font("Arial", "", 14)
        pdf.write(5, f"SSID: {ssid}\nPW: {pw}\n")
        pdf.image(f"{out_name}.png", 0, None, 200, 200, type="PNG")
        pdf.output(f"{out_name}.pdf", "F")

