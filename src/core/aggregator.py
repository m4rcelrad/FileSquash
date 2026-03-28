import os


def aggregate_files(target_dir: str, output_file: str, allowed_extensions: list[str], exclude_dirs: set[str]) -> None:
    with open(output_file, "w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk(target_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            for file in files:
                if any(file.endswith(ext) for ext in allowed_extensions):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, target_dir)

                    outfile.write(f"\n{'=' * 50}\n")
                    outfile.write(f"FILE: {rel_path}\n")
                    outfile.write(f"{'=' * 50}\n\n")

                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"[Error reading file: {e}]")

                    outfile.write("\n\n")
