


export default function get_exports(package_name: string): any {
    // @ts-ignore
    import * as lib from package_name
    const exports: string[] = []
    Object.keys(lib).forEach((key) => exports.push(key));

    return {}
}
