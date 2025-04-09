"use client";
import React, { useState, ChangeEvent, FormEvent, ChangeEventHandler } from "react";
import Input from "@/app/components/Input";
import Button from "@/app/components/Button";
import styles from "@/app/utils/css/dash/receiving.module.css";

interface FormData {
    ConsignmentNo?: string;
    InvoiceNo?: string;
    grade?: string;
    garden?: string;
    noOfBags?: number | '';
    palletWeight?: string;
    tareWeight?: string;
    netWeight?: string;
    grossWeight?: string;
}

interface TableData extends FormData {}
const initialFormData: FormData = {};

const Receive = () => {
    const [formData, setFormData] = useState<FormData>(initialFormData);
    const [tableData, setTableData] = useState<TableData[]>([]);
    const [selectedRowIndex, setSelectedRowIndex] = useState<number | null>(null);

    const handleInputChange = (
        event: ChangeEvent<HTMLInputElement | HTMLSelectElement>
    ) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleReadScale = () => {
        // Implementlogic to read data from the scale here
        console.log("Reading data from the scale...");
    };

    const handleAddRow = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setTableData([...tableData, formData]);
        setFormData({});
    };

    const handleDeleteRow = () => {
        if (selectedRowIndex !== null) {
            const newTableData = tableData.filter((_, index) => index !== selectedRowIndex);
            setTableData(newTableData);
            setSelectedRowIndex(null);
        } else {
            alert("Please select a row to delete.");
        }
    };

    const handleSubmitAll = () => {
        console.log("Submitting all data:", tableData);
    };
    return (
        <div className={styles.body}>
            <div className={styles.form}>
                <div className={styles.formContainer}>
                    <form onSubmit={handleAddRow} className={styles.gridForm}>
                        <div className={styles.field}>
                            <label>Consignment No:</label>
                            <Input type="text" name="ConsignmentNo" value={formData.ConsignmentNo || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Invoice No:</label>
                            <Input type="text" name="InvoiceNo" value={formData.InvoiceNo || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Grade:</label>
                            <select name="grade" value={formData.grade || ""} onChange={handleInputChange as ChangeEventHandler<HTMLSelectElement>}>
                            <option value="">Select Grade</option>
                            <option value="FBOP">FBOP</option>
                            <option value="BOP">BOP</option>
                            <option value="PF1">PF1</option>
                            <option value="Dust">Dust</option>
                            </select>
                        </div>
                        <div className={styles.field}>
                            <label>Garden</label>
                            <Input type="text" name="garden" value={formData.garden || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Number of Bags</label>
                            <Input type="number" name="noOfBags" value={formData.noOfBags === undefined ? '' : formData.noOfBags} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Pallet Weight</label>
                            <Input type="text" name="palletWeight" value={formData.palletWeight || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Tare Weight</label>
                            <Input type="text" name="tareWeight" value={formData.tareWeight || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        <div className={styles.field}>
                            <label>Net Weight</label>
                            <Input type="text" name="netWeight" value={formData.netWeight || ""} onChange={handleInputChange as ChangeEventHandler<HTMLInputElement>} />
                        </div>
                        {/* Button row */}
                        <div className={styles.buttonRow}>
                            <Button id="read-scale" type="button" onClick={handleReadScale}>Read Scale</Button>
                            <Button id="add-row" type="submit">Add Row</Button>
                            <Button id="delete-row" type="button" onClick={handleDeleteRow}>Delete Row</Button>
                        </div>
                    </form>
                </div>
            </div>

            {/* tea receiving data */}
            <div className={styles.tableData}>
                <div>
                    <table className={styles.receivingTable}>
                        <thead>
                            <tr>
                                <th className={styles.tableHeaderCell}>Consignment No</th>
                                <th className={styles.tableHeaderCell}>Invoice No</th>
                                <th className={styles.tableHeaderCell}>Grade</th>
                                <th className={styles.tableHeaderCell}>Garden</th>
                                <th className={styles.tableHeaderCell}>Number of Bags</th>
                                <th className={styles.tableHeaderCell}>Pallet Weight</th>
                                <th className={styles.tableHeaderCell}>Tare Weight</th>
                                <th className={styles.tableHeaderCell}>Net Weight</th>
                                <th className={styles.tableHeaderCell}>Gross Weight</th>
                                <th className={styles.tableHeaderCell}>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {tableData.map((row, index) => (
                                <tr
                                    key={index}
                                    onClick={() => setSelectedRowIndex(index)}
                                    className={selectedRowIndex === index ? styles.selectedRow : ''}
                                >
                                    <td className={styles.tableDataCell}>{row.ConsignmentNo}</td>
                                    <td className={styles.tableDataCell}>{row.InvoiceNo}</td>
                                    <td className={styles.tableDataCell}>{row.grade}</td>
                                    <td className={styles.tableDataCell}>{row.garden}</td>
                                    <td className={styles.tableDataCell}>{row.noOfBags}</td>
                                    <td className={styles.tableDataCell}>{row.palletWeight}</td>
                                    <td className={styles.tableDataCell}>{row.tareWeight}</td>
                                    <td className={styles.tableDataCell}>{row.netWeight}</td>
                                    <td className={styles.tableDataCell}>{row.grossWeight}</td>
                                    <td className={styles.tableDataCell}>
                                        {/* You could add a delete button here per row if preferred */}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    {tableData.length > 0 && (
                        <Button id="" className={styles.submitAllButton} onClick={handleSubmitAll}>Submit All Data</Button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Receive;